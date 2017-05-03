#11.1.5.4	Sentinel最大连接数
# 1.	问题描述 #

某准生产系统，测试运行一段时间后程序和命令行工具连接sentinel均报错，报错信息为：
	
	jedis.exceptions.JedisDataException: ERR max number of clients reached

此时应用创建redis新连接由于sentinel已经无法响应而无法找到master的IP与端口，因此无法连接redis，并且此时如果发生redis宕机亦无法进行生产切换。

# 2.	问题初步排查过程 #
首先，通过netstat对sentinel所监听端口26379进行连接数统计，此时连接则报错。如下图：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/other1.png) 

通过sentinel服务器端统计发现，redis sentinel 的连接中大部分都是来自于两台非同网段（中间有防火墙）的应用服务器连接（均为Established状态），并且来自其的连接也大约半个小时后稳步增加一次，而同网段的应用服务器连接sentinel的连接数基本保持一致。排除了应用的特殊性（采用的jedis版本和封装的工具类都是一样的）后，初步判断此问题与网络有关，更详细的说是连接数增加与防火墙切断连接后的重连有关。

# 3.	问题查证过程 #
此问题分为两个子问题：
1)	防火墙将TCP连接设置为无效时sentinel服务器为何没有断开连接，保持Established状态？
2)	为何连接数还会不断增加？

对于问题1) ，TCP在三次握手建立连接时OS会启动一个Timer来进行倒计时，经过一个设定的时间（这个时间建立socket的程序可以设置，如果没有设置则采用OS的参数tcp_keepalive_time，这个参数默认为7200s，即2小时）后这个连接还是没有数据传输，它就会以一定间隔（程序可以设定，如果没有设置则采用OS的参数tcp_keepalive_intvl，默认为75s）发出N（程序可以设定，如果没有设置则采用OS的参数tcp_keepalive_probes，默认为9次）次Keep Alive包。TCP连接就是通过上述的过程，在没有流量时是通过发送TCP Keep-Alive数据包，然后对方回应TCP Keep-Alive ACK来确定信道是否还在真实连接。通过查看Sentinel源代码，其默认是不开启Keepalive的（而jedis默认是开启的），并且默认对于不活动的连接也不会主动关闭的（timeout默认为0）。

对于防火墙，通过翻阅防火墙技术资料（详见下列描述，摘自：《Junos Enterprise Switching: A Practical Guide to Junos Switches and Certification》），我司采用的Juniper防火墙对于没有流量的TCP连接默认是30分钟，30分钟内没有流量就会断掉链路，而不会发送TCP Reset，同时在防火墙策略上并没有开长连接，使用的即为此默认设置。

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/other2.png) 

因此在防火墙每半个小时将连接置为无效时，sentinel同时又禁止了Keepalive（因为默认设置Keepalive为0，即disable发送Keepalive包）。应用服务器的jedis虽然开启了keepalive，但是它发送的keepalive包由于防火墙已经将此链路标记为无效，而无法发送到sentinel端，而且jedis由于采用了OS默认参数，因此需要等待tcp_keepalive_time（2小时）后才启动发送Keep Alive包进行探活的，在tcp_keepalive_time+tcp_keepalive_intvl*tcp_keepalive_probes=7895s=131.58分钟后，jedis端才会认定这个连接断掉而清理掉这个连接。简单的说就是jedis会在很长一段时间后才会发keepalive包，并且这个包也是发不到sentinel上的，而sentinel本身也不会发送keepalive包，所以从sentinel这端看连接一直存在，而从jedis那端看7895s之后就会清理一次连接。这也解释了为什么防火墙将TCP连接断开后，sentinel端的连接并没有释放。

对于问题2) ，翻阅jedis源代码，jedis通过连接sentinel并pubsub来监听集群事件，以确定是否发生了切换，并且拿到新的master 地址和端口。如果断开则会5秒后尝试重连（JedisSentinelPool.java）。

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/other3.png)  
因此，这是导致连接数不断上升的原因。
综上，防火墙相对频繁的断开和服务器不断重连导致在一个相对较短的时间内连接骤增，造成到达sentinel最大连接数，sentinel 的最大连接数在redis.h中定义，为10000：
 
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/other4.png)  

# 4.	问题解决过程 #
此系统由于访问关系与网段规划间的安全问题，必须跨越防火墙，因此试图从配置角度解决此问题。

首先，联系网络相关同事，进行网络变更，开启从应用服务器到sentinel的链路相对的长连接，即无流量超时而断开的时间设置为8小时。以此手段降低断开频率，以便缓解短时间内不断重试连接造成的sentinel连接增长。

然后，通过阅读redis源代码（net.c），发现，sentinel也采用了redis 所有参数设置（通过config.c的函数void loadServerConfigFromString(char *config)）。因此，通过设置redis 的下列两个参数可以解决这个问题，第一个参数是TCP Keepalive参数，此参数默认为0，也就是不发送keepalive。也就是改变OS默认的tcp_keepalive_time参数（在Unix C的socket编程中TCP_KEEPIDLE参数对应OS 的tcp_keepalive_time参数）。
 
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/other5.png)  

该参数的官方解释为：

	# TCP keepalive.
	#
	# If non-zero, use SO_KEEPALIVE to send TCP ACKs to clients in absence
	# of communication. This is useful for two reasons:
	#
	# 1) Detect dead peers.
	# 2) Take the connection alive from the point of view of network
	#    equipment in the middle.
	#
	# On Linux, the specified value (in seconds) is the period used to send ACKs.
	# Note that to close the connection the double of the time is needed.
	# On other kernels the period depends on the kernel configuration.
	#
	# A reasonable value for this option is 60 seconds.

我们设置为tcp-keepalive 60，加快回收连接速度，从网络断开到连接清理时间缩短为60+75*9=12.25分钟。

同时，通过设置maxclients为65536，增大sentinel最大连接数，使得在上述12.25分钟即使有某种异常导致sentinel连接数增加也不至于到达最大限制。此参数的官方解释为：

	################################### LIMITS ####################################
	
	# Set the max number of connected clients at the same time. By default
	# this limit is set to 10000 clients, however if the Redis server is not
	# able to configure the process file limit to allow for the specified limit
	# the max number of allowed clients is set to the current file limit
	# minus 32 (as Redis reserves a few file descriptors for internal uses).
	#
	# Once the limit is reached Redis will close all the new connections sending
	# an error 'max number of clients reached'.
	#
	maxclients 10000

对于redis 的timeout参数，由于启用这个参数有程序微小开销（会调用redis.c中的int clientsCronHandleTimeout(redisClient *c, mstime_t now_ms)），决定保持默认为0，而通过上述参数使用OS进行连接断开。

# 5.	问题解决结果 #
通过开发、网络和数据库团队的协同努力，配置上述参数和修改防火墙策略后，手动增加sentinel进程，超过原默认最大连接数10000后sentinel可以正常访问操作，并且通过tcpdump进行抓包，在指定时间内（1分钟），就有KeepAlive包对每个sentinel TCP连接进行探活，经过观察sentinel连接稳定，再未出现短时间内暴涨的情况。

# 6.	问题后续 #
在redis中默认不开启keepalive就是为了尽可能减小网络负载，榨干网络性能，尽可能达到redis的。在后续的程序运行中，如果发现网络是瓶颈时（在相当长的一段时间内不会），可以加大sentinel的keepalive参数，减小keepalive数据包的传输，这个修改是不影响redis对外服务的。

参考文档：
http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/

附录：如何用TCPDUMP进行keep alive抓包

	tcpdump -pni bond0 -v "src port 26379 and ( tcp[tcpflags] & tcp-ack != 0 and ( (ip[2:2] - ((ip[0]&0xf)<<2) ) - ((tcp[12]&0xf0)>>2) ) == 0 ) "

# 7.	问题再后续 #

我们后来在这个应用上发现一旦网络有抖动，sentinel的连接增加就回大幅度增加，后来通过jmap查看sentinelpool的实例竟然多达200多个，也就是说这个就是程序的问题，在sentinelpool上不应该多次实例化，而是采用已有连接进行重连。


