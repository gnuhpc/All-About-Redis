#11.1.4.8	master所在主机整体宕测试
恢复集群状态，2.128为主，2.129、2.130为从。此时，对2.128进行宕机测试，直接关闭电源。
主从切换至2.130,从2.129指向新的主：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest13.png)  
sentinel日志为：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest14.png) 