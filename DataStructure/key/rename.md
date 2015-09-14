#2.1.6	原子的重命名一个key
	
	rename oldkey newkey
	
如果newkey存在，将会被覆盖，返回1表示成功，0失败。可能是oldkey不存在或者和newkey相同

	
	renamenx oldkey newkey 
同上，但是如果newkey存在返回失败