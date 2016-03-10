# 2.7 HyperLogLog操作
HyperLogLog主要解决大数据应用中的非精确计数（可能多也可能少，但是会在一个合理的范围）操作，它可以接受多个元素作为输入，并给出输入元素的基数估算值，基数指的是集合中不同元素的数量。比如  {'apple', 'banana', 'cherry', 'banana', 'apple'} 的基数就是 3 。
HyperLogLog 的优点是，即使输入元素的数量或者体积非常非常大，计算基数所需的空间总是固定的、并且是很小的。在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

关于这个数据类型的误差：在一个大小为12k的key所存储的hyperloglog集合基数计算的误差是%0.81.

参考文献：http://highscalability.com/blog/2012/4/5/big-data-counting-how-to-count-a-billion-distinct-objects-us.html
