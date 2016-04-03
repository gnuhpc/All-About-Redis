#11.1.4.4	单从实例宕测试
接上，2.129为从，此时杀掉该进程，redis.log日志记录如下：

	[14984 | signal handler] (1434674492) Received SIGTERM scheduling shutdown...
	[14984] 19 Jun 08:41:32.545 # User requested shutdown...
	[14984] 19 Jun 08:41:32.545 * Calling fsync() on the AOF file.
	[14984] 19 Jun 08:41:32.545 * Saving the final RDB snapshot before exiting.
	[14984] 19 Jun 08:41:32.580 * DB saved on disk
	[14984] 19 Jun 08:41:32.580 # Redis is now ready to exit, bye bye...

此时集群正常提供对外服务，并不影响。
