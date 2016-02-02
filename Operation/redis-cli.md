#3.12	Redis-cli命令行其他操作

#### 1.	echo ：在命令行打印一些内容  ####
redis 127.0.0.1:6379> echo HongWan 
"HongWan" 

#### 2.	quit ：退出连接。 #### 
redis 127.0.0.1:6379> quit 

#### 3.	-x选项从标准输入（stdin）读取最后一个参数。 比如从管道中读取输入： ####
echo -en "chen.qun" | redis-cli -x set name

#### 4.	-r -i ####
-r 选项重复执行一个命令指定的次数。
-i 设置命令执行的间隔。
比如查看redis每秒执行的commands（qps）
redis-cli -r 100 -i 1 info stats | grep instantaneous_ops_per_sec
这个选项在编写一些脚本时非常有用

#### 5.	-c：开启reidis cluster模式，连接redis cluster节点时候使用。 ####

#### 6.	--rdb：获取指定redis实例的rdb文件,保存到本地。 ####
redis-cli -h 192.168.44.16 -p 6379 --rdb 6379.rdb

#### 7.	--slave ####
模拟slave从master上接收到的commands。slave上接收到的commands都是update操作，记录数据的更新行为。


#### 8.	--pipe ####
这个一个非常有用的参数。发送原始的redis protocl格式数据到服务器端执行。比如下面的形式的数据（linux服务器上需要用unix2dos转化成dos文件）。
linux下默认的换行是\n,windows系统的换行符是\r\n，redis使用的是\r\n.
echo -en '*3\r\n$3\r\nSET\r\n$3\r\nkey\r\n$5\r\nvalue\r\n' | redis-cli --pipe


###9.	-a ###
如果开启了requirepass，那么你如果希望调用或者自己编写一些外部脚本通过redis-cli进行操作或者监控redis，那么这个选项可以让你不用再手动输入auth。这个选项很普遍，但是往往被人忽视。

