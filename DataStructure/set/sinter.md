#2.4.8	集合交集
	sinter key1 key2...keyN 
返回所有给定key的交集

---
	sinterstore dstkey key1...keyN 
同sinter，但是会同时将交集存到dstkey下
