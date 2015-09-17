#2.5.3	增加score
	zincrby key incr member 
增加对应member的score值，然后移动元素并保持skip list保持有序。返回更新后的score值，可以为负数递减
