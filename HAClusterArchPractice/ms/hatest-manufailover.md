#11.1.4.2	手动切换测试
集群情况，2.128为主
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest1.png)

发起主动切换：

	127.0.0.1:26379> sentinel failover mymaster
	OK

查看sentinel日志：

		[1158] 19 Jun 08:14:38.504 # Executing user requested FAILOVER of 'mymaster'
		[1158] 19 Jun 08:14:38.507 # +new-epoch 29
		[1158] 19 Jun 08:14:38.507 # +try-failover master mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:38.581 # +vote-for-leader 7d60ccf8a9f9f81e5292a0dbde2c54c76a2bd265 29
		[1158] 19 Jun 08:14:38.581 # +elected-leader master mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:38.581 # +failover-state-select-slave master mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:38.655 # +selected-slave slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:38.655 * +failover-state-send-slaveof-noone slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:38.714 * +failover-state-wait-promotion slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:39.642 # +promoted-slave slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:39.642 # +failover-state-reconf-slaves master mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:39.705 * +slave-reconf-sent slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:40.645 * +slave-reconf-inprog slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:40.645 * +slave-reconf-done slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:40.735 # +failover-end master mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:14:40.735 # +switch-master mymaster 192.168.2.129 6379 192.168.2.128 6379
		[1158] 19 Jun 08:14:40.736 * +slave slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.128 6379
		[1158] 19 Jun 08:14:40.743 * +slave slave 192.168.2.129:6379 192.168.2.129 6379 @ mymaster 192.168.2.128 6379
		[1158] 19 Jun 08:27:56.524 # +new-epoch 30
		[1158] 19 Jun 08:27:57.519 # +config-update-from sentinel 192.168.2.128:26379 192.168.2.128 26379 @ mymaster 192.168.2.128 6379
		[1158] 19 Jun 08:27:57.519 # +switch-master mymaster 192.168.2.128 6379 192.168.2.129 6379
		[1158] 19 Jun 08:27:57.519 * +slave slave 192.168.2.130:6379 192.168.2.130 6379 @ mymaster 192.168.2.129 6379
		[1158] 19 Jun 08:27:57.524 * +slave slave 192.168.2.128:6379 192.168.2.128 6379 @ mymaster 192.168.2.129 6379

在2.129上看，集群已经切换过来：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest2.png)
