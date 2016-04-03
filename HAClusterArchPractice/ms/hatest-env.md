#11.1.4.1	测试环境介绍
	Master：192.168.2.128 （A）:6379
	Slave：192.168.2.129  （B）:6379
	Slave：192.168.2.130  （B）:6379
	Sentinel：三台机器的26379端口

sentinel的消息可以通过sentinel日志（/redis/log/sentinel.log）以及__sentinel__:hello订阅此频道进行查看。
