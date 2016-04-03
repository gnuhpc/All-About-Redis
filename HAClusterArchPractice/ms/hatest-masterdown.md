#11.1.4.3	主实例宕测试
接上，此时master为2.129，找出redis实例的pid，然后kill：

	[root@hadoop2 log]# ps -ef |grep redis-server
	root      11349   1157  1 Jun18 ?        00:15:45 /usr/bin/redis-server 0.0.0.0:6379
	root      14969  10433  0 08:33 pts/1    00:00:00 grep --color=auto redis-server
	[root@hadoop2 log]# kill 11349

此时查看sentinel日志：

	[1158] 19 Jun 08:33:57.953 # +sdown master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.025 # +odown master mymaster 192.168.2.129 6379 #quorum 3/2
	[1158] 19 Jun 08:33:58.025 # +new-epoch 31
	[1158] 19 Jun 08:33:58.025 # +try-failover master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.028 # +vote-for-leader 7d60ccf8a9f9f81e5292a0dbde2c54c76a2bd265 31
	[1158] 19 Jun 08:33:58.036 # 192.168.2.130:26379 voted for 7d60ccf8a9f9f81e5292a0dbde2c54c76a2bd265 31
	[1158] 19 Jun 08:33:58.037 # 192.168.2.128:26379 voted for 7d60ccf8a9f9f81e5292a0dbde2c54c76a2bd265 31
	[1158] 19 Jun 08:33:58.105 # +elected-leader master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.105 # +failover-state-select-slave master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.183 # +selected-slave slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.183 * +failover-state-send-slaveof-noone slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:58.267 * +failover-state-wait-promotion slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:59.039 # +promoted-slave slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:59.040 # +failover-state-reconf-slaves master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:59.104 * +slave-reconf-sent slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:33:59.245 # -odown master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:34:00.082 * +slave-reconf-inprog slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:34:00.082 * +slave-reconf-done slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:34:00.193 # +failover-end master mymaster 192.168.2.129 6379
	[1158] 19 Jun 08:34:00.193 # +switch-master mymaster 192.168.2.129 6379 192.168.2.128 6379
	[1158] 19 Jun 08:34:00.194 * +slave slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.128 6379
	[1158] 19 Jun 08:34:00.200 * +slave slave 192.168.2.129:6379 192.168.2.129 6379 @ mymaster 192.168.2.128 6379
	[1158] 19 Jun 08:34:03.319 # +sdown slave 192.168.2.129:6379 192.168.2.129 6379 @ mymaster 192.168.2.128 6379

从日志中可以看出已经切换到2.128，此时在2.128上看集群状态：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest3.png)

目前2.128为主，2.130为从，2.129上的redis宕掉。现在重启2.129上的redis实例，启动后该节点会从原先的主变为从，并对2.128进行同步，最后达到同步状态：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest4.png) 

查看redis.conf和redis-sentinel.conf，发现都被改写。
