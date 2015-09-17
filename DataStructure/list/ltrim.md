#2.3.5	截取list

	ltrim key start end 

保留指定区间内元素，成功返回1，key不存在返回错误。O(N)操作。



> 注意：N是被移除的元素的个数，不是列表长度。