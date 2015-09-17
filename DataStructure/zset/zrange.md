#2.5.5	获取排行榜
	zrange key start end 
类似lrange操作从集合中去指定区间的元素。返回的是有序结果

---
zrevrange key start end 
同上，返回结果是按score逆序的,如果需要得分则加上withscores  

> 注：index从start到end的所有元素
