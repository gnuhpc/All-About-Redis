#2.2.1	设置key对应的值为string类型的value
	set key value [ex 秒数] / [px 毫秒数]  [nx] /[xx]  

返回1表示成功，0失败
> 注: 如果ex,px同时写,以后面的有效期为准

----------

	setnx key value
仅当key不存在时才Set，如果key已经存在，返回0 。nx 是not exist的意思。

> 应用场景：用来选举Master或做分布式锁：所有Client不断尝试使用SetNx master myName抢注Master，成功的那位不断使用Expire刷新它的过期时间。如果Master倒掉了key就会失效，剩下的节点又会发生新一轮抢夺。

----------

	mset key1 value1 ... keyN valueN 
一次设置多个key的值，成功返回1表示所有的值都设置了，失败返回0表示没有任何值被设置

----------

	msetnx key1 value1 ... keyN valueN 
同上，但是不会覆盖已经存在的key

----------

SET 命令还支持可选的 NX 选项和 XX 选项，例如：SET nx-str "this will fail" XX   
- 如果给定了 NX 选项，那么命令仅在键 key 不存在的情况下，才进行设置操作；如果键 key 已经存在，那么 SET ... NX 命令不做动作（不会覆盖旧值）。
- 如果给定了 XX 选项，那么命令仅在键 key 已经存在的情况下，才进行设置操作；如果键 key 不存在，那么 SET ... XX 命令不做动作（一定会覆盖旧值）。在给定 NX 选项和 XX 选项的情况下，SET 命令在设置成功时返回 OK ，设置失败时返回 nil 。