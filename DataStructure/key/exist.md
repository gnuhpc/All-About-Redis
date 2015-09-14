# 2.1.1	列出key
    keys  *user*
    keys  *

有3个通配符 *, ? ,[]
- *: 通配任意多个字符
- ?: 通配单个字符
- []: 通配括号内的某1个字符

> 注：生产已经禁止。更安全的做法是采用scan，原理和操作如下：
> ![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/key/scan-intro.png)
> 
> 针对Keys的改进，支持分页查询Key。在迭代过程中，Keys有增删时不会要锁定写操作，数据集完整度不做任何保证，同一条key可能会被返回多次.
> 
> ![](https://raw.githubusercontent.com/gnuhpc/All-About-
Redis/master/DataStructure/key/scan.png)
> ![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/key/scan-compare.png)
> 对于其他危险的命令，新版本也进行了替代：
> ![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/key/scan-other.png)



redis-cli下的扫描:
    
    redis-cli --scan --pattern 'chenqun_*'
    

这是用scan命令扫描redis中的key，--pattern选项指定扫描的key的pattern。相比keys *pattern*模式,不会长时间阻塞redis而导致其他客户端的命令请求一直处于阻塞状态。

> 本页中采用了小象学院的两张片子，版权归 [http://www.chinahadoop.cn/](http://www.chinahadoop.cn/) 所有
