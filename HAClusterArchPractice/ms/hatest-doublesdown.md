#11.1.4.5	双从实例宕测试
接上，此时Master为2.128，还有一个活着的从2.130，集群状态如下：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest5.png)

此时，杀掉2.130的redis实例后，集群状态如下：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest6.png) 

此时由于配置了最小slave个数为1，已经不满足，因此集群变为只读状态：
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest7.png) 
