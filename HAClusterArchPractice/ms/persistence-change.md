#11.1.5.3	持久化动态修改
其实相对于VIP的切换，动态修改持久化则是比较常见的一个需求，一般在一主多从多Sentinel的HA环境中，为了性能常常在Master上关闭持久化，而在Slave上开启持久化，但是如果发生切换就必须有人工干预才能实现这个功能。可以利用client-reconfig-script自动化该进程，无需人工守护，我们就以RDB的动态控制为例：
Sentinel配置文件如下：

	sentinel client-reconfig-script mymaster /redis/script/rdbctl.sh

rdbctl.sh源代码：
	#!/bin/bash
	
	_DEBUG="on"
	DEBUGFILE="/smsred/redis-3.0.4/log/sentinel_failover.log"
	MASTERIP=${6}
	MASTERPORT=${7}
	SLAVEIP=${4}
	SLAVEPORT=${5}
	MASK='24'
	IFACE='bond0'
	MYIP=$(ip -4 -o addr show dev ${IFACE}| grep -v secondary| awk '{split($4,a,"/");print a[1]}')
	
	
	DEBUG () {
	        if [ "$_DEBUG" = "on" ]; then
	                echo `$@` >>  ${DEBUGFILE}
	        fi
	}
	
	 
	
	set -e
	DEBUG date
	DEBUG echo $@ 
	DEBUG echo "===Begin Failover==="
	#If Master
	
	if [ ${MASTERIP} = ${MYIP} ]; then
	       #Disable RDB
	       redis-cli -h ${MYIP} -p ${MASTERPORT} -a c1m2b3c4 config set save ""
	       DEBUG echo ${MYIP}
	       DEBUG echo "Disable Master RDB:" ${MYIP} ${MASTERPORT}
	        DEBUG echo "===End Failover==="
	        exit 0
	
	#Or Slave
	else
	        echo "test5" >> $DEBUGFILE
	       redis-cli -h ${MYIP} -p ${SLAVEPORT} -a c1m2b3c4 config set save "900 1 300 10 60 100000000"
	       DEBUG echo ${MYIP}
	       DEBUG echo "Enable Slave RDB:" ${MYIP} ${SLAVEPORT}
	        DEBUG echo "===End Failover==="
	        exit 0
	fi
	
	exit 1

原理和VIP切换一节基本一致，不再赘述。
