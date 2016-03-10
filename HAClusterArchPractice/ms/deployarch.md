#11.1.2.1	部署架构
部署架构上采用三台机器，一个Master接受写请求，两个Slave进行数据同步，三台机器上都部署sentinel（一般为奇数个，因为需要绝大部分进行投票才能failover）。（官方示例）具体架构如下图：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/deploy-1.png)
 
注意：如果有条件可以将sentinel多部署几个在客户端所在的应用服务器上，而不是与从节点部署在一起，这样避免整机宕机后sentinel和slave都减少而导致的切换选举sentinel无法超过半数。
