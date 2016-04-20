#3.2	事务
用Multi(Start Transaction)、Exec(Commit)、Discard(Rollback)实现。 在事务提交前，不会执行任何指令，只会把它们存到一个队列里，不影响其他客户端的操作。在事务提交时，批量执行所有指令。
一般情况下redis在接受到一个client发来的命令后会立即处理并返回处理结果，但是当一个client在一个连接中发出multi命令后，这个连接会进入一个事务上下文，该连接后续的命令并不是立即执行，而是先放到一个队列中。当从此连接受到exec命令后，redis会顺序的执行队列中的所有命令。并将所有命令的运行结果打包到一起返回给client.然后此连接就结束事务上下文。

Redis还提供了一个Watch功能，你可以对一个key进行Watch，然后再执行Transactions，在这过程中，如果这个Watched的值进行了修改，那么这个Transactions会发现并拒绝执行。

使用discard命令来取消一个事务。

注意：redis只能保证事务的每个命令连续执行（因为是单线程架构，在执行完事务内所有指令前是不可能再去同时执行其他客户端的请求的，也因此就不存在"事务内的查询要看到事务里的更新，在事务外查询不能看到"这个让人万分头痛的问题），但是如果事务中的一个命令失败了，并不回滚其他命令。另外，一个十分罕见的问题是当事务的执行过程中，如果redis意外的挂了。只有部分命令执行了，后面的也就被丢弃了。注意，如果是笔误，语法出现错误，则整个事务都无法执行。

一个简单案例表明出错也不会回滚：

	127.0.0.1:6379> del q1
	(integer) 0
	127.0.0.1:6379> exists q1
	(integer) 0
	127.0.0.1:6379> multi
	OK
	127.0.0.1:6379> rpush q1 bar
	QUEUED
	127.0.0.1:6379> scard q1
	QUEUED
	127.0.0.1:6379> exec
	1) (integer) 1
	2) (error) WRONGTYPE Operation against a key holding the wrong kind of value
	127.0.0.1:6379> exists q1
	(integer) 1


当然如果我们使用的append-only file方式持久化，redis会用单个write操作写入整个事务内容。即是是这种方式还是有可能只部分写入了事务到磁盘。发生部分写入事务的情况下，redis重启时会检测到这种情况，然后失败退出。可以使用redis-check-aof工具进行修复，修复会删除部分写入的事务内容。修复完后就能够重新启动了。
