#2.3.6	删除元素

	lrem key count value 
从key对应list中删除count个和value相同的元素。count为0时候删除全部，count为正，则删除匹配count个元素，如果为负数，则是从右侧扫描删除匹配count个元素。复杂度是O(N)，N是List长度，因为List的值不唯一，所以要遍历全部元素，而Set只要O(log(N))。

---
	lpop key 
从list的头部删除元素，并返回删除元素。如果key对应list不存在或者是空返回nil，如果key对应值不是list返回错误。

---
	rpop 
同上，但是从尾部删除。
