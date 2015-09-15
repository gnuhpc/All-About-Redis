#2.2.2	获取key对应的string值

	get key
如果key不存在返回nil

---

	getset key value 
原子的设置key的值，并返回key的旧值。如果key不存在返回nil。应用场景：设置新值，返回旧值，配合setnx可实现分布式锁。

分布式锁的思路：注意该思路要保证多台Client服务器的NTP一致。
1.	C3发送SETNX lock.foo 想要获得锁，由于C0还持有锁，所以Redis返回给C3一个0
2.	C3发送GET lock.foo 以检查锁是否超时了，如果没超时，则等待或重试。
3.	反之，如果已超时，C3通过下面的操作来尝试获得锁：
4.	GETSET lock.foo <current Unix time + lock timeout + 1>
5.	通过GETSET，C3拿到的时间戳如果仍然是超时的，那就说明，C3如愿以偿拿到锁了。
6.	如果在C3之前，有个叫C4的客户端比C3快一步执行了上面的操作，那么C3拿到的时间戳是个未超时的值，这时，C3没有如期获得锁，需要再次等待或重试。留意一下，尽管C3没拿到锁，但它改写了C4设置的锁的超时值，不过这一点非常微小的误差带来的影响可以忽略不计。

伪代码为：
	# get lock
	lock = 0
	while lock != 1:
	    timestamp = current Unix time + lock timeout + 1
	    lock = SETNX lock.foo timestamp
	    if lock == 1 or (now() > (GET lock.foo) and now() > (GETSET lock.foo timestamp)):
	        break;
	    else:
	        sleep(10ms)
	 
	# do your job
	do_job()
	 
	# release
	if now() < GET lock.foo:
	    DEL lock.foo

以上是一个单Server 的分布式锁思路，官网上还介绍了另一个单机使用超时方式进行的思路，和这个基本一致，并且在同一个文档中介绍了一个名为redlock的多Server容错型分布式锁的算法，同时列出了多语言的实现。这个算法的优势在于几个服务器可以有少量的时间差，不要求严格时间一致。

也可以设计一个按小时计算的计数器，可以用GetSet获取计数并重置为0。

---
	mget key1 key2 ... keyN 
一次获取多个key的值，如果对应key不存在，则对应返回nil
