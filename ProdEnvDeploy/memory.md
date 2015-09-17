#2.1	内存规划
一定要设置最大内存maxmemory参数，否则物理内存用爆了就会大量使用Swap，写RDB文件时的速度很慢。注意这个参数指的是info中的used_memory，在一些不利于jmalloc的时候，内存碎片会很大。

多留55%内存是最安全的。重写AOF文件和RDB文件的进程(即使不做持久化，复制到Slave的时候也要写RDB)会fork出一条新进程来，采用了操作系统的Copy-On-Write策略(子进程与父进程共享Page。如果父进程的Page-每页4K有修改，父进程自己创建那个Page的副本，不会影响到子进程)。

另外，需要考虑内存碎片，假设碎片为1.2，则如果机器为64G，那么64*45%/1.2 = 24G作为maxmemory是比较安全的规划。

留意Console打出来的报告，如"RDB: 1215 MB of memory used by copy-on-write"。在系统极度繁忙时，如果父进程的所有Page在子进程写RDB过程中都被修改过了，就需要两倍内存。

按照Redis启动时的提醒，设置 vm.overcommit_memory = 1 ，使得fork()一条10G的进程时，因为COW策略而不一定需要有10G的free memory。

当最大内存到达时，按照配置的Policy进行处理， 默认策略为volatile-lru，对设置了expire time的key进行LRU清除(不是按实际expire time)。如果沒有数据设置了expire time或者policy为noeviction，则直接报错，但此时系统仍支持get之类的读操作。 另外还有几种policy，比如volatile-ttl按最接近expire time的，allkeys-lru对所有key都做LRU。注意在一般的缓存系统中，如果没有设置超时时间，则lru的策略需要设置为allkeys-lru，并且应用需要做好未命中的异常处理。特殊的，当redis当做DB时，请使用noneviction策略，但是需要对系统内存监控加强粒度。
