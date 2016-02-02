6.1.4	查看统计信息

	Mrds:6379> info
在cli下执行info。
	
	info Replication

只看其中一部分。
	
	config resetstat
重新统计。
    # Server
    redis_version:2.8.19 ###redis版本号
    redis_git_sha1:00000000  ###git SHA1
    redis_git_dirty:0   ###git dirty flag
    redis_build_id:78796c63e58b72dc
    redis_mode:standalone   ###redis运行模式
    os:Linux 2.6.32-431.el6.x86_64 x86_64   ###os版本号
    arch_bits:64  ###64位架构
    multiplexing_api:epoll  ###调用epoll算法
    gcc_version:4.4.7   ###gcc版本号
    process_id:25899   ###服务器进程PID
    run_id:eae356ac1098c13b68f2b00fd7e1c9f93b1c6a2c   ###Redis的随机标识符(用于sentinel和集群)
    tcp_port:6379   ###Redis监听的端口号
    uptime_in_seconds:6419 ###Redis运行时长(s为单位)
    uptime_in_days:0  ###Redis运行时长(天为单位)
    hz:10
    lru_clock:10737922  ###以分钟为单位的自增时钟,用于LRU管理
    config_file:/etc/redis/redis.conf   ###redis配置文件
     
    # Clients
    connected_clients:1   ###已连接客户端的数量（不包括通过从属服务器连接的客户端）这个参数也要一定关注，有飙升和明显下降时都会有问题。即使不操作
    client_longest_output_list:0   ###当前连接的客户端中最长的输出列表
    client_biggest_input_buf:0   ###当前连接的客户端中最大的。输出缓存
    blocked_clients:0  ###正在等待阻塞命令（BLPOP、BRPOP、BRPOPLPUSH）的客户端的数量 需监控
     
    # Memory
    used_memory:2281560   ###由 Redis 分配器分配的内存总量，以字节（byte）为单位
    used_memory_human:2.18M   ###以更友好的格式输出redis占用的内存
    used_memory_rss:2699264   ###从操作系统的角度，返回 Redis 已分配的内存总量（俗称常驻集大小）。这个值和 top 、 ps 等命令的输出一致，包含了used_memory和内存碎片。
    used_memory_peak:22141272  ### Redis 的内存消耗峰值（以字节为单位）
    used_memory_peak_human:21.12M  ###以更友好的格式输出redis峰值内存占用
    used_memory_lua:35840  ###LUA引擎所使用的内存大小
    mem_fragmentation_ratio:1.18  ###   =used_memory_rss /used_memory 这两个参数都包含保存用户k-v数据的内存和redis内部不同数据结构需要占用的内存，并且RSS指的是包含操作系统给redis实例分配的内存，这里面还包含不连续分配所带来的开销。因此在理想情况下， used_memory_rss 的值应该只比 used_memory 稍微高一点儿。当 rss > used ，且两者的值相差较大时，表示存在（内部或外部的）内存碎片。内存碎片的比率可以通过 mem_fragmentation_ratio 的值看出。当 used > rss 时，表示 Redis 的部分内存被操作系统换出到交换空间了，在这种情况下，操作可能会产生明显的延迟。可以说这个值大于1.5或者小于1都是有问题的。当大于1.5的时候需要择机进行服务器重启。当小于1的时候需要对redis进行数据清理
    mem_allocator:jemalloc-3.6.0
    
    # Persistence
    loading:0  ###记录服务器是否正在载入持久化文件，1为正在加载
    rdb_changes_since_last_save:0   ###距离最近一次成功创建持久化文件之后，产生了多少次修改数据集的操作
    rdb_bgsave_in_progress:0   ###记录了服务器是否正在创建 RDB 文件，1为正在进行
    rdb_last_save_time:1420023749  ###最近一次成功创建 RDB 文件的 UNIX 时间戳
    rdb_last_bgsave_status:ok   ###最近一次创建 RDB 文件的结果是成功还是失败,失败标识为err，这个时候写入redis 的操作可能会停止，因为默认stop-writes-on-bgsave-error是开启的，这个时候如果需要尽快恢复写操作，可以手工将这个选项设置为no。
    rdb_last_bgsave_time_sec:0  ###最近一次创建 RDB 文件耗费的秒数
    rdb_current_bgsave_time_sec:-1  ###如果服务器正在创建 RDB 文件，那么这个域记录的就是当前的创建操作已经耗费的秒数
    aof_enabled:1   ###AOF 是否处于打开状态，1为启用
    aof_rewrite_in_progress:0   ###服务器是否正在创建 AOF 文件
    aof_rewrite_scheduled:0   ###RDB 文件创建完毕之后，是否需要执行预约的 AOF 重写操作（因为在RDB时aof的rewrite会被阻塞一直到RDB结束）
    aof_last_rewrite_time_sec:-1  ###最近一次创建 AOF 文件耗费的时长
    aof_current_rewrite_time_sec:-1  ###如果服务器正在创建 AOF 文件，那么这个域记录的就是当前的创建操作已经耗费的秒数
    aof_last_bgrewrite_status:ok  ###最近一次创建 AOF 文件的结果是成功还是失败
    aof_last_write_status:ok 
    aof_current_size:176265  ###AOF 文件目前的大小
    aof_base_size:176265  ###服务器启动时或者 AOF 重写最近一次执行之后，AOF 文件的大小
    aof_pending_rewrite:0  ###是否有 AOF 重写操作在等待 RDB 文件创建完毕之后执行
    aof_buffer_length:0   ###AOF 缓冲区的大小
    aof_rewrite_buffer_length:0  ###AOF 重写缓冲区的大小
    aof_pending_bio_fsync:0  ###后台 I/O 队列里面，等待执行的 fsync 调用数量
    aof_delayed_fsync:0###被延迟的 fsync 调用数量
    loading_start_time:1441769386   loading启动时间戳
    loading_total_bytes:1787767808   loading需要加载数据量
    loading_loaded_bytes:1587418182  已经加载的数据量
    loading_loaded_perc:88.79 加载百分比
    loading_eta_seconds:7   剩余时间
    
    # Stats
    total_connections_received:8466  ###服务器已接受的连接请求数量，注意这是个累计值。
    total_commands_processed:900668   ###服务器已执行的命令数量，这个数值需要持续监控，如果在一段时间内出现大范围波动说明系统要么出现大量请求，要么出现执行缓慢的操作。
    instantaneous_ops_per_sec:1   ###服务器每秒钟执行的命令数量
    total_net_input_bytes:82724170
    total_net_output_bytes:39509080
    instantaneous_input_kbps:0.07
    instantaneous_output_kbps:0.02
    rejected_connections:0  ###因为最大客户端数量限制而被拒绝的连接请求数量
    sync_full:2
    sync_partial_ok:0
    sync_partial_err:0
    expired_keys:0   ###因为过期而被自动删除的数据库键数量
    evicted_keys:0   ###因为最大内存容量限制而被驱逐（evict）的键数量。这个数值如果不是0则说明maxmemory被触发，并且	evicted_keys一直大于0，则系统的latency增加，此时可以临时提高最大内存，但这只是临时措施，需要从应用着手分析。
    keyspace_hits:0  ###查找数据库键成功的次数。可以计算命中率
    keyspace_misses:500000   ###查找数据库键失败的次数。
    pubsub_channels:0  ###目前被订阅的频道数量
    pubsub_patterns:0  ###目前被订阅的模式数量
    latest_fork_usec:402  ###最近一次 fork() 操作耗费的毫秒数
     
    # Replication
    role:master   ###如果当前服务器没有在复制任何其他服务器，那么这个域的值就是 master ；否则的话，这个域的值就是 slave 。注意，在创建复制链的时候，一个从服务器也可能是另一个服务器的主服务器
    connected_slaves:2   ###2个slaves
    slave0:ip=192.168.65.130,port=6379,state=online,offset=1639,lag=1
    slave1:ip=192.168.65.129,port=6379,state=online,offset=1639,lag=0
    master_repl_offset:1639
    repl_backlog_active:1
    repl_backlog_size:1048576
    repl_backlog_first_byte_offset:2
    repl_backlog_histlen:1638
     
    # CPU
    used_cpu_sys:41.87  ###Redis 服务器耗费的系统 CPU
    used_cpu_user:17.82  ###Redis 服务器耗费的用户 CPU
    used_cpu_sys_children:0.01  ###后台进程耗费的系统 CPU
    used_cpu_user_children:0.01  ###后台进程耗费的用户 CPU
     
    # Keyspace
    db0:keys=3101,expires=0,avg_ttl=0   ###keyspace 部分记录了数据库相关的统计信息，比如数据库的键数量、数据库过期键数量等。对于每个数据库，这个部分都会添加一行此信息

