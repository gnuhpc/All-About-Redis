#7.6	模拟AOF加载情形
	debug loadaof

清空当前数据库，重新从aof文件里加载数据库
emptyDb();
loadAppendOnlyFile();
