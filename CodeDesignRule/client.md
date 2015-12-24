#4.7	客户端推荐
##4.7.1 Redis-Python驱动的安装和使用
	unzip redis-py-master.zip 
	cd redis-py-master/
	sudo python setup.py install

完成后import redis即可。


      
##4.7.2 Redis-Java客户端推荐

1.	Jedis ：https://github.com/xetorthio/jedis  重点推荐
2.	Spring Data redis ：https://github.com/spring-projects/spring-data-redis  使用Spring框架时推荐
3.	Redisson ：https://github.com/mrniko/redisson 分布式锁、阻塞队列的时重点推荐


##4.7.3	Redis-C客户端推荐
Hiredis是redis数据库一个官方推荐的C语言redis client库。
