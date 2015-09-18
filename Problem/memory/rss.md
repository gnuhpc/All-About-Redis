#6.3.9	Rss增加，内存碎片增加
此时可以选择时间进行redis服务器的重新启动，并且注意在rss突然降低观察是否swap被使用，以确定并非是因为swap而导致的rss降低。

一个典型的例子是：http://grokbase.com/t/gg/redis-db/14ag5n9qhv/redis-memory-fragmentation-ratio-reached-5000


