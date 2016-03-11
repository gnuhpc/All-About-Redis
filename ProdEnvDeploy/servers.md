#5.3	服务器部署位置
尽可能把client和server部署在同一台机器上，比如都部署在app server，或者一个网段中，减少网络延迟对于redis的影响。


如果是同一台机器，又想榨干redis性能可以考虑采用UNIX domain sockets配置方式，配置方式如下
	# 0 = do not listen on a port
	port 0
	
	# listen on localhost only
	bind 127.0.0.1
	
	# create a unix domain socket to listen on
	unixsocket /tmp/redis.sock
	
	# set permissions for the socket
	unixsocketperm 755

这样的配置方式在没有大量pipeline下会有一定性能提升，具体请参见http://redis.io/topics/benchmarks：

另外，对于混合部署即redis和应用部署在同一台服务器上，那么可能会出现如下的情况：

>出现瞬时 Redis 大量连接和处理超时，应用业务线程被阻塞，导致服务拒绝，过一段时间可能又自动恢复了。这种瞬时故障非常难抓现场，一天来上几发就会给人业务不稳定的感受，而一般基础机器指标的监控周期在分钟级。瞬时故障可能发生在监控的采集间隙，所以只好上脚本在秒级监控日志，发现瞬时出现大量 Redis 超时错误，就收集当时应用的 JVM 堆栈、内存和机器 CPU Load 等各项指标。终于发现瞬时故障时刻 Redis 机器 CPU Load 出现瞬间飙升几百的现象，应用和 Redis 混合部署时应用可能瞬间抢占了全部 CPU 导致 Redis 没有 CPU 资源可用。而应用处理业务的逻辑又可能需要访问 Redis，而 Redis 又没有 CPU 资源可用导致超时，这不就像一个死锁么。搞清楚了原因其实解决方法也简单，就是分离应用和 Redis 的部署，各自资源隔离

>出处：
http://mp.weixin.qq.com/s?__biz=MzAxMTEyOTQ5OQ==&mid=402004912&idx=1&sn=7517696a86f54262e60e1b5636d6cbe0&3rd=MzA3MDU4NTYzMw==&scene=6#rd

因此在混合部署下要对极限性能进行监控，提前将可能出现性能问题的应用迁移出来。

