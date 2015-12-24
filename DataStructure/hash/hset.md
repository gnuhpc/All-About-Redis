#2.6.1	设置hash值
	
	hset key field value 
设置hash field为指定值，如果key不存在，则先创建。

	hsetnx 
设置hash field为指定值，如果 key 不存在，则先创建。如果 field已经存在，返回0，nx是not exist的意思。

