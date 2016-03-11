#5.4	持久化设置
RDB和AOF两者毫无关系，完全独立运行，如果使用了AOF，重启时只会从AOF文件载入数据，不会再管RDB文件。在配置上有三种选择：不持久化，RDB，RDB+AOF。官方不推荐只开启AOF（因为恢复太慢另外如果aof引擎有bug），除非明显的读多写少的应用。
开启AOF时应当关闭AOF自动rewrite，并在crontab中启动在业务低峰时段进行的bgrewrite。
如果在一台机器上部署多个redis实例，则关闭RDB和AOF的自动保存（save "", auto-aof-rewrite-percentage 0），通过crontab定时调用保存：
    
    m h * * * redis-cli -p <port> BGSAVE
    m h */4 * * redis-cli -p <port> BGREWRITEAOF

持久化的部署规划上，如果为主从复制关系，建议主关闭持久化。

