#3.13.2	AOF相关操作
	BGREWRITEAOF
在后台执行一个 AOF文件重写操作


动态关闭AOF：
	
	redis-cli config set appendonly no
动态打开AOF：

	redis-cli config set appendonly yes
永久关闭AOF：

	sed -e '/appendonly/ s/^#*/#/' -i /etc/redis/redis.conf  （默认是关闭的）
永久打开AOF：

	将appendonly yes设置在redis.conf中

