#11.1.4.13	附：sentinel.conf被修改后的含义
port 26379
dir "/var/lib/redis/tmp"
sentinel monitor mymaster 192.168.65.128 6379 2
sentinel config-epoch mymaster 18   ###确认mymater SDOWN时长
sentinel leader-epoch mymaster 18  ###同时一时间最多18个slave可同时更新配置,建议数字不要太大,以免影响正常对外提供服务
sentinel known-slave mymaster 192.168.65.129 6379   ###已知的slave
sentinel known-slave mymaster 192.168.65.130 6379   ###已知的slave
sentinel known-sentinel mymaster 192.168.65.130 26379 be964e6330ee1eaa9a6b5a97417e866448c0ae40    ###已知slave的唯一id
sentinel known-sentinel mymaster 192.168.65.129 26379 3e468037d5dda0bbd86adc3e47b29c04f2afe9e6  ###已知slave的唯一id
sentinel current-epoch 18  ####当前可同时同步的salve数最大同步阀值
