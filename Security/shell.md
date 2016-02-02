#9.1	Shell提权问题
问题报告：http://drops.wooyun.org/papers/3062
	
	
问题分析：Redis 安全模型的观念是: “请不要将Redis暴露在公开网络中, 因为让不受信任的客户接触到Redis是非常危险的” 。The Redis security model is: “it’s totally insecure to let untrusted clients access the system, please protect it from the outside world yourself”. 因此最近爆出的问题也非redis本身产品问题，属于不当配置。
	
问题规避：

1.	使用redis单独用户和组进行安全部署，并且在OS层面禁止此用户ssh登陆，这就从根本上防止了root用户启停redis带来的风险。 
2.	修改默认端口，降低网络简单扫描危害。
3.	修改绑定地址，如果是本地访问要求绑定本地回环。 
4.	要求设置密码，并对配置文件访问权限进行控制，因为密码在其中是明文。 
5.	HA环境下主从均要求设置密码。 另外，我们建议在网络防火墙层面进行保护，杜绝任何部署在外网直接可以访问的redis的出现。 
