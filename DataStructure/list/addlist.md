#2.3.1	添加元素
	lpush key string 
在key对应list的头部添加字符串元素，返回1表示成功，0表示key存在且不是list类型。注意：江湖规矩一般从左端Push，右端Pop，即LPush/RPop。

---
	lpushx
也是将一个或者多个value插入到key列表的表头，但是如果key不存在，那么就什么都不在，返回一个false【rpushx也是同样】

---
	rpush key string 
同上，在尾部添加

---
	linsert
在key对应list的特定位置之前或之后添加字符串元素 , 例如
    
    redis 127.0.0.1:6379linsert mylist3 before "world" "there" 
    