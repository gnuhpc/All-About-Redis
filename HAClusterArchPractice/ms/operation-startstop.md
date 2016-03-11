#11.1.3.2	启停redis
supervisorctl -c /redis/conf/redis-supervisord.conf start redis
supervisorctl -c /redis/conf/redis-supervisord.conf stop redis
supervisorctl -c /redis/conf/redis-supervisord.conf restart redis
