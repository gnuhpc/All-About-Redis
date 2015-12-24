#6.2.2	检查网络情况
可以在系统不繁忙或者临时下线前检测客户端和server或者proxy 的带宽：

1)使用 iperf -s 命令将 Iperf 启动为 server 模式:

	iperf –s
	————————————————————
	Server listening on TCP port 5001
	TCP window size: 8.00 KByte (default)
	————————————————————
2)启动客户端，向IP为10.230.48.65的主机发出TCP测试，并每2秒返回一次测试结果，以Mbytes/sec为单位显示测试结果：

	iperf -c 10.230.48.65 -f M -i 2
