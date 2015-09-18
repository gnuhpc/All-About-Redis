#6.1.6	查看客户端
	client list
列出所有连接

	client kill 
杀死某个连接， 例如`CLIENT KILL 127.0.0.1:43501`

	client getname #
获取连接的名称 默认nil

	client setname "名称" 
设置连接名称,便于调试
