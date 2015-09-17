#3.3	流水线
利用流水线（pipeline）的方式从client打包多条命令一起发出，不需要等待单条命令的响应返回，而redis服务端会处理完多条命令后会将多条命令的处理结果打包到一起返回给客户端：

	cat data.txt | redis-cli –pipe

在选择开源redis开发库时需要着重注意是否支持pipeline，常见的jedis可以支持。
