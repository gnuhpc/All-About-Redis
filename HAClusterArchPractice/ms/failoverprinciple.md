#11.1.1.2	基本切换原理
在切换中，配置文件是会被动态修改的，例如当发生主备切换时候，配置文件中的master会被修改为另外一个slave。这样，之后sentinel如果重启时，就可以根据这个配置来恢复其之前所监控的redis集群的状态。
在sentinel切换过程中有三大步骤：
1.	判断是否下线（老主是否真的咽气驾崩）
每个sentinel在监控的时候，每秒对主进行一次ping命令，如果多次ping的响应时间超过了配置文件中的down-after-milliseconds，那么这个哨兵就会认为被监控的实例是SDown状态（Subjectively Down，主观down，SDOWN）。
这个时候此sentinel会判断此master是否真的挂了——即可以设置成ODOWN（Objectively Down，客观down，ODOWN）。设置成ODOWN的条件是除了当前sentinel认为此master SDOWN，还必须有其他sentinel认为此master SDOWN，当认为SDOWN的sentinel的个数等于或超过配置文件中monitor master最后的那个参数quorum后，就sentinel就会认为此master是ODOWN。
被标记为ODOWN的另一个效应是：在一般情况下，每个 Sentinel 进程会以每 10 秒一次的频率向它已知的所有主实例和从实例发送 INFO 命令。 当一个主实例被 Sentinel实例标记为客观下线时， Sentinel 向ODOWN Master的所有从实例发送 INFO 命令的频率会从 10 秒一次改为每秒一次。
2.	进行投票选举主持切换的sentinel（选举一个长老，由它来钦点新帝王）
当master被认为是ODOWN的时候，可能需要进行failover，但是并不是odown了就可以执行failover，因为可能有多个sentinel都认为master是odown了，这时候就需要选举一个sentiel来执行failover。也就是说切换之前要先选举一个sentinel来主持切换，条件是必须有>=max(quorum, num(sentinels)/2 +1)的sentinel都同意某一个sentinel主持failover，那么这个sentinel就可以主持failover，超过半数这个条件就能限制住此时刻只有一个sentinel来操作。
这个也是通过is-master-down-by-addr消息进行更新每个sentinel的选举的leader。每个sentinel都有一个epoch，这个东西相当于一个时间戳，是递增的值，如果集群正常的话，所有的sentinel的这个值都是一样的。当master出现异常后，每个sentinel后自增这个值，如果一直没有选举出来leader的话，这个值会跟随这time event的轮询，每次加一，在设定的故障迁移超时时间的两倍之后， 重新尝试当选。同时is-master-down-by-addr会把这个值发送到其他的sentinel，其他的sentinel收到这个消息后，会判断自己的epoch和消息中的epoch，如果自己的epoch小于消息中的epoch，那么其他的sentinel就会选举传递消息的这个sentinel。最终会大部分sentinel都同意一个较大的epoch的sentinel主持failover。

3.	进行切换，并其他实例同步新Master（新帝王登基，其余藩王宣誓效忠新帝王）
这个主持切换的sentinel选出一个从redis实例，并将它升级为Master。首先是要下面的条件按照如下条件筛选备选node：
1)	slave节点状态处于S_DOWN,O_DOWN,DISCONNECTED的除外
2)	最近一次ping应答时间不超过5倍ping的间隔（假如ping的间隔为1秒，则最近一次应答延迟不应超过5秒，redis sentinel默认为1秒）
3)	info_refresh应答不超过3倍info_refresh的间隔（原理同2,redis sentinel默认为10秒）
4)	slave节点与master节点失去联系的时间不能超过（ (now - master->s_down_since_time) + (master->down_after_period * 10)）。总体意思是说，slave节点与master同步太不及时的（比如新启动的节点），不应该参与被选举。
5)	Slave priority不等于0（这个是在配置文件中指定，默认配置为100）。
 
然后再从备选node中，按照如下顺序选择新的master
1)	较低的slave_priority（这个是在配置文件中指定，默认配置为100）
2)	较大的replication offset（每个slave在与master同步后offset自动增加）
3)	较小的runid（每个redis实例，都会有一个runid,通常是一个40位的随机字符串,在redis启动时设置，重复概率非常小）
4)	如果以上条件都不足以区别出唯一的节点，则会看哪个slave节点处理之前master发送的command多，就选谁。
主持切换的sentinel向被选中的从redis实例发送 SLAVEOF NO ONE 命令，让它转变为Master。然后通过发布与订阅功能，将更新后的配置传播给所有其他 Sentinel，其他 Sentinel 对它们自己的配置进行config-rewrite。随后sentinel向已下线的Master的从服务器发送SLAVEOF命令，让它们去复制新Master。

注意：sentinel failover-timeout这个选项有四个含义，有必要在此翻译一下
1)	对于一个sentinel选出的同一个master进行再次的failover尝试所需要的时间——这个参数值的两倍。
2)	当sentinel发现一个slave错误的复制了一个错的主时sentinel会强迫其复制正确的主的时间。
3)	取消一个已经开始但是还没有引起任何配置改变的failover所需要的时间。
4)	等待所有slave被重新配置为新主的slave而所需要的最大时间。注意即使超过了这个时间sentinel也会最终配置slave去同步最新的master
