#11.1.3.11	判断主从是否完全一致
	dbsize

查看key 的数目

	debug digest

对整个数据库的数据，产生一个摘要，可用于验证两个redis数据库数据是否一致
127.0.0.1:6379> debug digest
7164ae8b6730c8bcade46532e5e4a8015d4cccfb
127.0.0.1:6379> debug digest
7164ae8b6730c8bcade46532e5e4a8015d4cccfb
