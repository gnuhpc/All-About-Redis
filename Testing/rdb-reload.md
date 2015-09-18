#7.5	模拟RDB load情形
	debug reload

save当前的rdb文件，并清空当前数据库，重新加载rdb，加载与启动时加载类似，加载过程中只能服务部分只读请求（比如info、ping等）：
rdbSave();
emptyDb();
rdbLoad();
