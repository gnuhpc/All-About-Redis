#2.7.2	返回给定 HyperLogLog 的基数估算值
	PFCOUNT key [key ...]
当只给定一个 HyperLogLog 时，命令返回给定 HyperLogLog 的基数估算值。当给定多个 HyperLogLog 时，命令会先对给定的 HyperLogLog 进行并集计算，得出一个合并后的 HyperLogLog ，然后返回这个合并 HyperLogLog 的基数估算值作为命令的结果（合并得出的 HyperLogLog 不会被储存，使用之后就会被删掉）。
当命令作用于单个 HyperLogLog 时， 复杂度为 O(1) ， 并且具有非常低的平均常数时间。
当命令作用于多个 HyperLogLog 时， 复杂度为 O(N) ，并且常数时间也比处理单个 HyperLogLog 时要大得多。
