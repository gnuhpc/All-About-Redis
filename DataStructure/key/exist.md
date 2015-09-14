# 2.1.1	列出key
    keys  *user*
    keys  *

有3个通配符 *, ? ,[]
- *: 通配任意多个字符
- ?: 通配单个字符
- []: 通配括号内的某1个字符

> 注：生产已经禁止。更安全的做法是采用scan，原理和操作如下：
> ![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/key/scan-intro.png)
