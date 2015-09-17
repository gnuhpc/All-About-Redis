#2.4.2	移除元素
	srem key member
成功返回1，如果member在集合中不存在或者key不存在返回0，如果key对应的不是set类型的值返回错误
