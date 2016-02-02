#3.13.1	RDB相关操作
BGSAVE：后台子进程进行RDB持久化
SAVE：主进程进行RDB，生产环境千万别用，服务器将无法响应任何操作。
LASTSAVE： 返回上一次成功SAVE的Unix时间



动态关闭RDB：

	redis-cli config set save ""

动态设置RDB：
	
	redis-cli config set save "900 1"
永久关闭RDB：

	sed -e '/save/ s/^#*/#/' -i /etc/redis/redis.conf
永久设置RDB：
	
	在redis.conf中设置save选项

查看RDB是否打开：
	
	redis-cli config get save
空的即是关闭，有数字的都是打开的。

