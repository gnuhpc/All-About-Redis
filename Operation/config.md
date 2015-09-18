#3.3	查看和修改配置
查看：

    config get ：获取服务器配置信息。 
    redis 127.0.0.1:6379> config get dir 
    config get *：查看所有配置

修改：

    临时设置：config set
    永久设置：config rewrite，将目前服务器的参数配置写入redis conf.
