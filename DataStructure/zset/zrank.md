#2.5.4	获取排名
	zrank key member 
返回指定元素在集合中的排名（下标，注意不是分数）,集合中元素是按score从小到大排序的

---
	zrevrank key member 
同上,但是集合中元素是按score从大到小排序
