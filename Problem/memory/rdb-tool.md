#8.3.4	dump.rdb文件成生内存报告（rdb-tool）
	# rdb -c memory ./dump.rdb > redis_memory_report.csv
	# sort -t, -k4nr redis_memory_report.csv
