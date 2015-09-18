#3.11	性能测试命令
	redis-benchmark -q -r 100000 -n 100000 -c 50
比如：开100条线程(默认50)，SET 1千万次(key在0-1千万间随机)，key长21字节，value长256字节的数据。-r指的是使用随机key的范围。

	redis-benchmark -t SET -c 100 -n 10000000 -r 10000000 -d 256

也可以直接执行lua脚本模拟客户端
	
	redis-benchmark -n 100000 -q script load "redis.call('set','foo','bar')"

注意：Redis-Benchmark的测试结果提供了一个保证你的 Redis-Server 不会运行在非正常状态下的基准点，但是你永远不要把它作为一个真实的“压力测试”。压力测试需要反应出应用的运行方式，并且需要一个尽可能的和生产相似的环境。
