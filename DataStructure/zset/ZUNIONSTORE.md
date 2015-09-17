#2.5.10	评分的聚合
	ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]

例如：

    127.0.0.1:6379> zrangebyscore votes -inf inf withscores
    1) "sina"
    2) "1"
    3) "google"
    4) "5"
    5) "baidu"
    6) "10"
    127.0.0.1:6379> zrangebyscore visits -inf inf withscores
    1) "baidu"
    2) "1"
    3) "google"
    4) "5"
    5) "sina"
    6) "10"
    127.0.0.1:6379> zunionstore award 2 visits votes weights 1 2 aggregate sum
    (integer) 3
    127.0.0.1:6379> zrangebyscore award -inf inf withscores
    1) "sina"
    2) "12"
    3) "google"
    4) "15"
    5) "baidu"
    6) "21"

一个小技巧是如果需要对评分进行倍加，则使用如下的方法：
    
    127.0.0.1:6379>zrangebyscore visits -inf inf withscores
    1) "baidu"
    2) "1"
    3) "google"
    4) "5"
    5) "sina"
    6) "10"
    127.0.0.1:6379>zunionstore visits 1 visits weights 2
    (integer) 3
    127.0.0.1:6379>zrangebyscore visits -inf inf withscores
    1) "baidu"
    2) "2"
    3) "google"
    4) "10"
    5) "sina"
    6) "20"
    