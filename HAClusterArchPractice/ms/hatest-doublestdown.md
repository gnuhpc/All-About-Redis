#11.1.4.7	双sentinel宕测试
恢复集群状态，2.128为主，2.129、2.130为从。此时，将2.128的sentinel和2.129的sentinel都宕掉。此时主从集群读写均正常。
在双方sentinel宕机时，杀掉master，主从集群切换失效，原因是因为设置sentinel 的quorum为2，最少有两个sentinel活集群才正常切换。
