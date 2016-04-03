#11.1.4.11	 quorum测试
在一个如下的四节点环境中，

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest27.png) 

如果sentinel monitor的quorum设置为3，则宕机一台后再宕机，此时还剩余两台，存在两个sentinel，两个slave。由于quorum为3，而必须有>=max(quorum, num(sentinels)/2 +1) = max(3,2) = 3个sentinel都同意其中某一个sentinel主持failover，因此此时无sentinel可主持切换，因此测试表明，没有新的master被选出来，此时只能手动通过slaveof命令设置主从，并且手动切换（redis、sentinel和都应用不用重启）：

	首先修改redis：
	任意选取剩余的其中一个节点进行：slaveof no one
	其他节点：slaveof 192.168.145.135 6379
	
	找一个从节点上的sentinel，进入sentinel：
	redis-cli -p 26379
	进行主动切换：
	sentinel failover mymaster
	然后再在两个sentinel上重新发现集群：
	sentinel reset mymaster

	检查集群状态。


如果sentinel monitor的quorum设置为2，则宕机一台后再宕机，此时还剩余两台，存在两个sentinel，两个slave。由于quorum为2，必须有>=max(quorum, num(sentinels)/2 +1)=max(2,2) =2个的sentinel都同意其中某一个sentinel主持failover，因此此时存在sentinel可主持切换，因此测试表明，新的master被选出来。

但是设置为2有一个危险就是如果出现如下的网络隔离状况：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest28.png)
 
集群就会脑裂，就会出现两个master。因此，生产上为了万无一失，宁可牺牲掉一定的高可用容错度也要避免脑裂。如果希望两台宕机依然可以切换，最好的方案不是降低quorum而是增多sentinel的个数，这个建议也是antirez在stackoverflow中回答一个人的提问时给的建议（http://stackoverflow.com/questions/27605843/redis-sentinel-last-node-doesnt-become-master#）。
如下场景测试：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest29.png) 
此时其中两台宕机，必须有>=max(quorum, num(sentinels)/2 +1)=max(3,3) =3个的sentinel都同意其中某一个sentinel主持failover，因此此时存在sentinel可主持切换，测试结果表明此种部署方案可以正常切换。
