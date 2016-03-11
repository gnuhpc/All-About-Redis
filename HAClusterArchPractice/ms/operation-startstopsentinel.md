#11.1.3.4	启停sentinel
supervisorctl -c /redis/conf/redis-supervisord.conf start redis-sentinel
supervisorctl -c /redis/conf/redis-supervisord.conf stop redis-sentinel
supervisorctl -c /redis/conf/redis-supervisord.conf restart redis-sentinel
