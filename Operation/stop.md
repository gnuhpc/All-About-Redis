#3.2	停止

	redis-cli shutdown

sentinel方法一样，只是需要执行sentinel的连接端口
> 
> 注意：正确关闭服务器方式是redis-cli shutdown 或者 kill，都会graceful shutdown，保证写RDB文件以及将AOF文件fsync到磁盘，不会丢失数据。 如果是粗暴的Ctrl+C，或者kill -9 就可能丢失。
> 