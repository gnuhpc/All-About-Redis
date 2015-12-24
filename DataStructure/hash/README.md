底层实现是hash table，一般操作复杂度是O(1)，要同时操作多个field时就是O(N)，N是field的数量。应用场景：土法建索引。比如User对象，除了id有时还要按name来查询。

可以有如下的数据记录:
(String) user:101 -> {"id":101,"name":"calvin"...}
(String) user:102 -> {"id":102,"name":"kevin"...}
(Hash) user:name:index-> "calvin"->101, "kevin" -> 102
