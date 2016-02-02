#3.11	性能测试命令
	redis-benchmark -q -r 100000 -n 100000 -c 50
比如：开100条线程(默认50)，SET 1千万次(key在0-1千万间随机)，key长21字节，value长256字节的数据。-r指的是使用随机key的范围。

	redis-benchmark -t SET -c 100 -n 10000000 -r 10000000 -d 256

也可以直接执行lua脚本模拟客户端
	
	redis-benchmark -n 100000 -q script load "redis.call('set','foo','bar')"

注意：Redis-Benchmark的测试结果提供了一个保证你的 Redis-Server 不会运行在非正常状态下的基准点，但是你永远不要把它作为一个真实的“压力测试”。压力测试需要反应出应用的运行方式，并且需要一个尽可能的和生产相似的环境。


Redis-benchmark还有一个作用就是灌数据，例如下列测试场景，我们对某个系统常用redis API进行测试，下列是一个测试hget、hset的过程，我们首先利用__rand_int__进行随机整数获取，对myhash这个key进行测试数据灌入（这也就测试了hset性能），然后再对其进行hget：

	MSMSAPP1:/tmp # ./redis-benchmark -a pass -h 40.XXX.XXX.141 -p 16XXXX -r 500000 -n 500000 hset myhash __rand_int__ __rand_int__ 
	====== hset myhash __rand_int__ __rand_int__ ====== 
	500000 requests completed in 18.74 seconds 
	50 parallel clients 
	3 bytes payload 
	keep alive: 1 
	
	23.53% <= 1 milliseconds 
	95.84% <= 2 milliseconds 
	97.62% <= 3 milliseconds 
	97.71% <= 4 milliseconds 
	97.80% <= 5 milliseconds 
	97.84% <= 6 milliseconds 
	97.84% <= 8 milliseconds 
	97.85% <= 9 milliseconds 
	97.85% <= 10 milliseconds 
	97.85% <= 11 milliseconds 
	97.86% <= 12 milliseconds 
	97.88% <= 13 milliseconds 
	97.90% <= 14 milliseconds 
	97.92% <= 15 milliseconds 
	97.94% <= 16 milliseconds 
	97.94% <= 20 milliseconds 
	97.95% <= 21 milliseconds 
	97.95% <= 22 milliseconds 
	97.99% <= 23 milliseconds 
	98.01% <= 24 milliseconds 
	98.11% <= 25 milliseconds 
	98.43% <= 26 milliseconds 
	98.85% <= 27 milliseconds 
	99.17% <= 28 milliseconds 
	99.43% <= 29 milliseconds 
	99.54% <= 30 milliseconds 
	99.68% <= 31 milliseconds 
	99.77% <= 32 milliseconds 
	99.81% <= 33 milliseconds 
	99.85% <= 34 milliseconds 
	99.85% <= 35 milliseconds 
	99.87% <= 36 milliseconds 
	99.88% <= 37 milliseconds 
	99.89% <= 38 milliseconds 
	99.90% <= 39 milliseconds 
	99.90% <= 40 milliseconds 
	99.91% <= 44 milliseconds 
	99.91% <= 45 milliseconds 
	99.91% <= 46 milliseconds 
	99.92% <= 47 milliseconds 
	99.92% <= 48 milliseconds 
	99.93% <= 49 milliseconds 
	99.93% <= 50 milliseconds 
	99.95% <= 51 milliseconds 
	99.96% <= 52 milliseconds 
	99.96% <= 53 milliseconds 
	99.97% <= 54 milliseconds 
	99.98% <= 55 milliseconds 
	100.00% <= 55 milliseconds 
	26679.47 requests per second 
	
	MSMSAPP1:/tmp # ./redis-benchmark -a pass 40.XXX.XXX.141 -p 16XXXX -r 500000 -n 500000 hget myhash __rand_int__ __rand_int__ 
	====== hget myhash __rand_int__ __rand_int__ ====== 
	500000 requests completed in 13.83 seconds 
	50 parallel clients 
	3 bytes payload 
	keep alive: 1 
	
	74.29% <= 1 milliseconds 
	98.29% <= 2 milliseconds 
	98.45% <= 3 milliseconds 
	98.45% <= 4 milliseconds 
	98.45% <= 5 milliseconds 
	98.46% <= 11 milliseconds 
	98.46% <= 12 milliseconds 
	98.48% <= 15 milliseconds 
	98.49% <= 16 milliseconds 
	98.50% <= 22 milliseconds 
	98.50% <= 23 milliseconds 
	98.57% <= 24 milliseconds 
	98.81% <= 25 milliseconds 
	99.16% <= 26 milliseconds 
	99.45% <= 27 milliseconds 
	99.71% <= 28 milliseconds 
	99.84% <= 29 milliseconds 
	99.91% <= 30 milliseconds 
	99.94% <= 31 milliseconds 
	99.94% <= 32 milliseconds 
	99.95% <= 33 milliseconds 
	99.96% <= 34 milliseconds 
	99.96% <= 44 milliseconds 
	99.96% <= 45 milliseconds 
	99.97% <= 49 milliseconds 
	99.97% <= 50 milliseconds 
	99.99% <= 55 milliseconds 
	100.00% <= 56 milliseconds 
	100.00% <= 56 milliseconds 
	36145.45 requests per second 

注意：上述测试由于是取的随机值，因此hget可能没有命中，同时payload比较小，所以这是个极限性能。

另外，还有一个工具是RedisLab放出来的，我并没有进行测试
参见：https://github.com/RedisLabs/memtier_benchmark

