#8.3.5	query在线分析
	redis-cli MONITOR | head -n 5000 | ./redis-faina.py
