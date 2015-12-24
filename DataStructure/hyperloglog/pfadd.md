#2.7.1	将元素添加至 HyperLogLog
	PFADD key element [element ...]
这个命令可能会对 HyperLogLog 进行修改，以便反映新的基数估算值，如果 HyperLogLog 的基数估算值在命令执行之后出现了变化， 那么命令返回 1 ， 否则返回 0 。 命令的复杂度为 O(N) ，N 为被添加元素的数量。
