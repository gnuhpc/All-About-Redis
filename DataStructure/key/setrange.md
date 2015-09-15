#2.2.6	改写字符串
	SETRANGE key offset value
用value 参数覆写(overwrite)给定key 所储存的字符串值，从偏移量offset 开始。 不存在的key 当作空白字符串处理。可以用作append：

![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/setrange.png)

>注意: 如果偏移量>字符长度, 该字符自动补0x00，注意它不会报错
>![](https://raw.githubusercontent.com/gnuhpc/All-About-Redis/master/DataStructure/string/setrange0.png)