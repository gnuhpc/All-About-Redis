#6.2.4	检查连接数
查看info里面的total_connections_received，如果该值不断升高，则需要修改应用，采用连接池方式进行，因为频繁关闭再创建连接redis的开销很大。
