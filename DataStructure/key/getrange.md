#2.2.7	返回子字符串
GETRANGE key start end

返回key 中字符串值的子字符串，字符串的截取范围由start 和end 两个偏移量决定(包括start 和end 在内)。可以使用负值，字符串右面下标是从-1开始的。

注意返回值处理：	
1: start>=length, 则返回空字符串
2: stop>=length,则截取至字符结尾
3: 如果start 所处位置在stop右边, 返回空字符串
