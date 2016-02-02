#2.6	具体设置参数
详见我行自制安装包conf目录中的各个配置文件和上线前检查表格。

redis参数设置技巧列表：
1.	Daemonize
这个参数在使用supervisord这种进程管理工具时一定要设置为no，否则无法使用这些工具将redis启动。

2.	Dir
	RDB的位置，一定要事先创建好，并且启动redis 的用户对此目录要有读写权限。
3.	Include
如果是多实例的话可以将公共的设置放在一个conf文件中，然后引用即可：
include /redis/conf/redis-common.conf  
