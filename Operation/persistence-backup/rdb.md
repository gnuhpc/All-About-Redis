#3.13.1	RDB相关操作
BGSAVE：后台子进程进行RDB持久化
SAVE：主进程进行RDB，生产环境千万别用，服务器将无法响应任何操作。
LASTSAVE： 返回上一次成功SAVE的Unix时间

---
	redis-cli config set save ""
动态关闭RDB
