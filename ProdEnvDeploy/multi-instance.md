#2.5	多实例配置
如果一台机器上防止多个redis实例，为了防止上下文切换导致的开销，可以采用taskset。taskset是LINUX提供的一个命令(ubuntu系统可能需要自行安装，schedutils package)。他可以让某个程序运行在某个（或）某些CPU上。

1）显示进程运行的CPU （6137为redis-server的进程号）

    [redis@hadoop1 ~]$ taskset  -p 6137
    pid 6137's current affinity mask: f 
显示结果的f实际上是二进制4个低位均为1的bitmask，每一个1对应于1个CPU，表示该进程在4个CPU上运行

2）指定进程运行在某个特定的CPU上

	[redis@hadoop1 ~]$ taskset -pc 3 6137
	pid 6137's current affinity list: 0-3
	pid 6137's new affinity list: 3 
注：3表示CPU将只会运行在第4个CPU上（从0开始计数）。

3）进程启动时指定CPU

	taskset -c 1 ./redis-server ../redis.conf

参数：OPTIONS
-p, --pid
 operate on an existing PID and not launch a new task

-c, --cpu-list
 specify a numerical list of processors instead of a bitmask. The list may contain multiple items, separated by comma, and ranges. For example, 0,5,7,9-11.
