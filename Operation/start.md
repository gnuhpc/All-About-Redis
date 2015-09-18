#3.1	启动
## 3.1.1	启动redis ##
    $ redis-server redis.conf

常见选项：
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --slaveof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose

## 3.1.2	启动redis-sentinel ##

       ./redis-server /etc/sentinel.conf –sentinel
       ./redis-sentinel /etc/sentinel.conf

部署后可以使用sstart对redis 和sentinel进行拉起，使用sctl进行supervisorctl的控制。（两个alias）
