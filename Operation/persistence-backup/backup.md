#3.13.3	备份
对于RDB和AOF，都是直接拷贝文件即可，可以设定crontab进行定时备份：
cp /var/lib/redis/dump.rdb /somewhere/safe/dump.$(date +%Y%m%d%H%M).rdb
