#8.3.7	统计生产上比较大的key
	./redis-cli --bigkeys
对redis中的key进行采样，寻找较大的keys。是用的是scan方式，不用担心会阻塞redis很长时间不能处理其他的请求。执行的结果可以用于分析redis的内存的只用状态，每种类型key的平均大小。
