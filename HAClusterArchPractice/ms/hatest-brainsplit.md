#11.1.4.10	脑裂测试
恢复集群状态，2.128为主，2.129、2.130为从。首先进行一个从网络分离的测试：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest17.png)   
此时集群状态为（从master看）：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest18.png)   
此时切断2.130这个链路，2.128和2.129分别为主从形成一个集群，2.130会失败，因为没有足够的sentinel进行投票完成failover。剩余集群如下：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest19.png)   
第三台机器则为slave失败状态：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest20.png)   
此时由于没有发生切换，因此对应用没有影响。

另一种情况，如果将主机网络断开，剩余两个从成为一个新的集群，其中一个从（2.129）成为主：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest21.png) 

原来的主机则为没有slave的主：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest22.png) 

此时由于没有可用的slave，旧主无法写入（实际上由于网络断开也根本无法访问，因此从网络和数据库本身都不具有可写性）：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest23.png)  
新主从可以接受读写请求：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest24.png) 
此时如果旧主的网络恢复，由于它的epoch比较旧，因此会成为从，将部分同步（psync）网络宕期间产生的新数据。
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest25.png)  

从上述两种情况测试，此架构不会导致双主对外服务，也不会因为网络恢复而数据混乱。

脑裂的场景还可以进行的一个测试时多个sentinel，例如下列架构（为了便于测试在两台机器上开多端口模拟多台机器）：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest26.png)  
 
这个场景配置Quorum=3.
此时切断两台机器的通信网络（模拟两个机房之间通信中断），左边的机器（模拟主机房）集群不会受到影响，右边的机器（模拟灾备机房）由于不够大多数因此不会产生新的Master。
