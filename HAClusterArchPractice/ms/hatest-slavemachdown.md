#11.1.4.9	slave所在主机整体宕测试
恢复集群状态，2.128为主，2.129、2.130为从。此时直接关闭2.129，这时相当于一个redis slave进程和一个sentinel进程宕。主不受影响，并且感知到一个从已经宕机。
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest15.png)   
sentinel日志记录了此事件。
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/HAClusterArchPractice/ms/hatest16.png)  
