#2.5.2	删除元素
	zrem key member 
1表示成功，如果元素不存在返回0

---
	zremrangebyrank key min max 
删除集合中排名在给定区间的元素

---
	zremrangebyscore key min max 
删除集合中score在给定区间的元素
