#2.2	网卡RPS设置
RPS就是让网卡使用多核CPU的。传统方法就是网卡多队列（RSS，需要硬件和驱动支持），RPS则是在系统层实现了分发和均衡。如果对redis网络处理能力要求高或者在生产上发现cpu0的，可以在OS层面打开这个内核功能。
 

设置脚本：

    #!/bin/bash  
    # Enable RPS (Receive Packet Steering)  
    
    rfc=32768
    cc=$(grep -c processor /proc/cpuinfo)  
    rsfe=$(echo $cc*$rfc | bc)  
    sysctl -w net.core.rps_sock_flow_entries=$rsfe  
    for fileRps in $(ls /sys/class/net/eth*/queues/rx-*/rps_cpus)  
    do
    echo fff > $fileRps  
    done
     
    for fileRfc in $(ls /sys/class/net/eth*/queues/rx-*/rps_flow_cnt)  
    do
    echo $rfc > $fileRfc  
    done
     
    tail /sys/class/net/eth*/queues/rx-*/{rps_cpus,rps_flow_cnt}
    