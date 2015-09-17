#2.3.8	阻塞队列

	blpop key1...keyN timeout 

从左到右扫描返回对第一个非空list进行lpop操作并返回，比如blpop list1 list2 list3 0 ,如果list不存在list2,list3都是非空则对list2做lpop并返回从list2中删除的元素。如果所有的list都是空或不存在，则会阻塞timeout秒，timeout为0表示一直阻塞。当阻塞时，如果有client对key1...keyN中的任意key进行push操作，则第一在这个key上被阻塞的client会立即返回（返回键和值）。如果超时发生，则返回nil。有点像unix的select或者poll。

	brpop
同blpop，一个是从头部删除一个是从尾部删除。

> 注意：不要采用其作为ajax的服务端推送，因为连接有限，遇到问题连接直接打满。


BLPOP/BRPOP 的先到先服务原则
如果有多个客户端同时因为某个列表而被阻塞，那么当有新值被推入到这个列表时，服务器会按照先到先服务（first in first service）原则，优先向最早被阻塞的客户端返回新值。举个例子，假设列表 lst 为空，那么当客户端 X 执行命令 BLPOP lst timeout 时，客户端 X 将被阻塞。在此之后，客户端 Y 也执行命令 BLPOP lst timeout ，也因此被阻塞。如果这时，客户端 Z 执行命令 RPUSH lst "hello" ，将值 "hello" 推入列表 lst ，那么这个 "hello" 将被返回给客户端 X ，而不是客户端 Y ，因为客户端 X 的被阻塞时间要早于客户端 Y 的被阻塞时间。

rpoplpush/brpoplpush：rpoplpush srckey destkey 从srckey对应list的尾部移除元素并添加到destkey对应list的头部,最后返回被移除的元素值，整个操作是原子的.如果srckey是空或者不存在返回nil，注意这是唯一一个操作两个列表的操作，用于两个队列交换消息。

应用场景：task + bak 双链表完成工作任务转交的安全队列，保证原子性。
业务逻辑:
1: Rpoplpush task bak
2: 接收返回值,并做业务处理
3: 完成时用LREM消掉。如不成功或者如果集群管理(如zookeeper)发现worker已经挂掉,下次从bak表里取任务

另一个应用场景是循环链表：
127.0.0.1:6379> lrange list 0 -1
1) "c"
2) "b"
3) "a"
127.0.0.1:6379> rpoplpush list list
"a"
127.0.0.1:6379> lrange list 0 -1
1) "a"
2) "c"
3) "b"
