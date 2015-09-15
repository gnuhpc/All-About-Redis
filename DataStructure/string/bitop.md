#2.2.10	位操作

**注意：位操作中的位置是反过来的，offset过大,则会在中间填充0，比如 SETBIT bit 0 1，此时bit为10000000，此时再进行SETBIT bit 7 1，此时bit为10000001。offset最大2^32-1。**
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/bit2.png)


	GETBIT key offset / SETBIT key offset value
设置某个索引的位为0/1

	bitcount
对位进行统计
![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/bit1.png)

	bitop
对1个或多个key对应的值进行AND/OR/XOR/NOT操作

注意: 
>1.bitop操作避免阻塞应尽量移到slave上操作.
>2.对于NOT操作, key不能多个
