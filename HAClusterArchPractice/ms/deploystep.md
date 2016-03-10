#11.1.2.6	部署步骤 
解压下列压缩包至/tmp/redis目录，以符合上述目录结构：


部署相关组件：
cd /tmp/redis/deploy
./deploy.sh 

修改Master配置文件redis.conf，注释掉包含slaveof的语句。
修改Slave配置文件redis.conf，添加slaveof masterIP port，指定主从
修改三台机器的sentinel配置文件，指定主服务器的IP和端口：
sentinel monitor mymaster masterIP port 2

然后使用supervisord重新启动。
