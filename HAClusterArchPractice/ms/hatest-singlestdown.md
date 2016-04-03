#11.1.4.6	单sentinel宕测试
恢复集群状态，2.128为主，2.129、2.130为从。
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest8.png)  
此时，从2.128上看sentinel状态：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest9.png)   
由于sentinel都是对等的，在此选择对2.128上的sentinel进行进程宕测试：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest10.png) 
此时，本节点sentinel日志为：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest11.png) 
其他节点sentinel日志为：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest12.png) 
表示2.128上的sentnel已经宕。
此时集群读写正常，在一个sentinel宕机的基础上宕master后切换正常。
