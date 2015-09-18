#3.4	批量执行操作
使用telnet也可以连接redis-server。并且在脚本中使用nc命令进行redis操作也是很有效的：

    gnuhpc@gnuhpc:~$ (echo -en "ping\r\nset key abc\r\nget key\r\n";sleep 1) | nc 127.0.0.1 6379
    +PONG
    +OK
    $3
    abc

另一个方式是使用pipeline：
    
    在一个脚本中批量执行多个写入操作:
    先把插入操作放入操作文本insert.dat：
    set a b
    set 1 2
    set h w
    set f u
    然后执行命令:cat insert.bat | ./redis-cli --pipe，或者如下脚本：
    #!/bin/sh
    host=$1
    port=$；
    password=$3
    cat insert.dat | ./redis-cli -h $host -p $port -a $password --pipe
