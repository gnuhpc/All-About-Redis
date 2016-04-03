#11.1.5.1	只读性
主从复制架构下，默认Slave是只读的，如果写入则会报错：

	127.0.0.1:6379> set foo bar
	(error) READONLY You can't write against a read only slave.

注意这个行为是可以修改的，虽然这样的修改没有意义：

	127.0.0.1:6379> CONFIG SET slave-read-only no
	OK
	127.0.0.1:6379> set foo bar
	OK

