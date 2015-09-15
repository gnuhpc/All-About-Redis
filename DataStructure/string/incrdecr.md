	incr key 
对key的值做加加操作,并返回新的值。注意incr一个不是int的value会返回错误，incr一个不存在的key，则设置key为1。范围为64有符号，-9223372036854775808~9223372036854775807。

----------

	decr key 
同上，但是做的是减减操作，decr一个不存在key，则设置key为-1

---

	incrby key integer 
同incr，加指定值 ，key不存在时候会设置key，并认为原来的value是 0

---
	decrby key integer 
同decr，减指定值。decrby完全是为了可读性，我们完全可以通过incrby一个负值来实现同样效果，反之一样。

---
	incrbyfloat key floatnumber
针对浮点数

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/incrfloat.png) 

----

哪些可以被操作呢？

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/incr1.png) 


----
这个操作的应用场景：计数器
