#11.1.5.2	虚拟IP切换
在sentinel进行切换时还会自动调用一个脚本（如果设置的话），做一些自动化操作，比如如果我们需要一个虚拟IP永远飘在Master上（这个VIP可不是被应用用来连接redis 的，用过的人都知道连接redis sentinel并不依赖于VIP的），那么可以在sentinel配置文件中配置：
	
	sentinel client-reconfig-script mymaster /redis/script/failover.sh

在发生主从切换，Master发生变化时，该脚本会被sentinel进行调用，调用的参数如其配置文件所描述的：

	# The following arguments are passed to the script:
	#
	# <master-name> <role> <state> <from-ip> <from-port> <to-ip> <to-port>
	#
	# <state> is currently always "failover"
	# <role> is either "leader" or "observer"
	# 
	# The arguments from-ip, from-port, to-ip, to-port are used to communicate
	# the old address of the master and the new address of the elected slave
	# (now a master).

因此，我们可以在failover.sh中进行判断，如果该脚本所运行的主机IP等于新的Master IP，那么将VIP加上，如果不等于，则该机器为Slave，就去掉VIP。通过这种方式进行VIP的切换：

	#!/bin/sh
	_DEBUG="on"
	DEBUGFILE=/tmp/sentinel_failover.log
	VIP='192.168.2.120'
	MASTERIP=${6}
	MASK='24'
	IFACE='eno33554960'
	MYIP=$(ip -4 -o addr show dev ${IFACE}| grep -v secondary| awk '{split($4,a,"/");print a[1]}')
	 
	DEBUG () {
	        if [ "$_DEBUG" = "on" ]; then
	                echo `$@` >>  ${DEBUGFILE}
	        fi
	}
	 
	set -e
	DEBUG date 
	DEBUG echo $@  
	DEBUG echo "Master: ${MASTERIP} My IP: ${MYIP}"
	if [ ${MASTERIP} = ${MYIP} ]; then
	        if [ $(ip addr show ${IFACE} | grep ${VIP} | wc -l) = 0 ]; then
	                /sbin/ip addr add ${VIP}/${MASK} dev ${IFACE}
			DEBUG date
	                DEBUG echo "/sbin/ip addr add ${VIP}/${MASK} dev ${IFACE}"
			DEBUG date
			DEBUG echo "IP Arp cleaning: /usr/sbin/arping -q -f -c 1 -A ${VIP} -I ${IFACE}" 
	                /usr/sbin/arping -q -f -c 1 -A ${VIP} -I ${IFACE}
			DEBUG date 
			DEBUG echo "IP Failover finished!"
	        fi
	        exit 0
	else
	        if [ $(ip addr show ${IFACE} | grep ${VIP} | wc -l) != 0 ]; then
	                /sbin/ip addr del ${VIP}/${MASK} dev ${IFACE}
	                DEBUG echo "/sbin/ip addr del ${VIP}/${MASK} dev ${IFACE}"
	        fi
	        exit 0
	fi
	exit 1


最早这样的用法是一个日本人写的blog，请参见：http://blog.youyo.info/blog/2014/05/24/redis-cluster/
