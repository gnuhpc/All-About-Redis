#11.1.4.14	附：sentinel事件含义
    +reset-master <instance details> -- 当master被重置时.
    +slave <instance details> -- 当检测到一个slave并添加进slave列表时.
    +failover-state-reconf-slaves <instance details> -- Failover状态变为reconf-slaves状态时
    +failover-detected <instance details> -- 当failover发生时
    +slave-reconf-sent <instance details> -- sentinel发送SLAVEOF命令把它重新配置时
    +slave-reconf-inprog <instance details> -- slave被重新配置为另外一个master的slave，但数据复制还未发生时。
    +slave-reconf-done <instance details> -- slave被重新配置为另外一个master的slave并且数据复制已经与master同步时。
    -dup-sentinel <instance details> -- 删除指定master上的冗余sentinel时 (当一个sentinel重新启动时，可能会发生这个事件).
    +sentinel <instance details> -- 当master增加了一个sentinel时。
    +sdown <instance details> -- 进入SDOWN状态时;
    -sdown <instance details> -- 离开SDOWN状态时。
    +odown <instance details> -- 进入ODOWN状态时。
    -odown <instance details> -- 离开ODOWN状态时。
    +new-epoch <instance details> -- 当前配置版本被更新时。
    +try-failover <instance details> -- 达到failover条件，正等待其他sentinel的选举。
    +elected-leader <instance details> -- 被选举为去执行failover的时候。
    +failover-state-select-slave <instance details> -- 开始要选择一个slave当选新master时。
    no-good-slave <instance details> -- 没有合适的slave来担当新master
    selected-slave <instance details> -- 找到了一个适合的slave来担当新master
    failover-state-send-slaveof-noone <instance details> -- 当把选择为新master的slave的身份进行切换的时候。
    failover-end-for-timeout <instance details> -- failover由于超时而失败时。
    failover-end <instance details> -- failover成功完成时。
    switch-master <master name> <oldip> <oldport> <newip> <newport> -- 当master的地址发生变化时。通常这是客户端最感兴趣的消息了。
    +tilt -- 进入Tilt模式。
    -tilt -- 退出Tilt模式。
