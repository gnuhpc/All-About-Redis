#2.1.6	原子的重命名一个key
	
	rename oldkey newkey
	
如果newkey存在，将会被覆盖，返回OK表示成功，如果失败，则可能是oldkey不存在或者和newkey相同，返回具体错误信息。

	
	renamenx oldkey newkey 
同上，成功返回1，失败返回0，如果newkey存在的话。
