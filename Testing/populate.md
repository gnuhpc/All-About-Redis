#7.4	快速产生测试数据
	debug populate

测试利器，快速产生大量的key

    127.0.0.1:6379> debug populate 10000
    OK
    127.0.0.1:6379> dbsize
    (integer) 10000
