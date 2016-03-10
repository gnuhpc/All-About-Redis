#11.1.2.7	配置文件
首先，一个sentinel可以配置多个master。一个master的配置如下：

	port 26379
	###定义目录存放
	dir "/redis"
	###监控mymaster(可自定义-但只能包括A-z 0-9和”._-”)，注意quorum只影响ODOWN的判断，但是不影响failover，发生failover的条件必须是半数sentinel认为老Master已经ODOWN。此参数建议设置为sentinel/2+1的数值，否则可能会产生脑裂。
	sentinel monitor mymaster 192.168.145.131 6379 2
	###mymaster多久不响应认为SDOWN，设置为3100也就是说3次ping失败后认为SDOWN
	sentinel down-after-milliseconds mymaster 3100
	###如果在该时间（ms）内未能完成failover操作，则认为该failover失败
	sentinel failover-timeout mymaster 15000
	
	###在执行故障转移时， 最多可以有多少个从Redis实例在同步新的主实例， 在从Redis实例较多的情况下这个数字越小，同步的时间越长，完成故障转移所需的时间就越长
	sentinel parallel-syncs mymaster 1
	
	###reconfig的时候执行的脚本（选配）
	sentinel client-reconfig-script mymaster /redis/script/failover.sh
	
	###出现任何sentinel在warning事件时候执行的脚本（选配）
	sentinel notification-script mymaster  /redis/script/notify.sh
	
	####日志位置
	logfile "/redis/log/sentinel.log"
