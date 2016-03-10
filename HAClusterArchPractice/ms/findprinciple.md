#12.1.1.1	发现原理

Sentinel发现分为发现从服务器和发现其他sentinel服务两类：
- Sentinel实例可以通过询问主实例来获得所有从实例的信息
- Sentinel进程可以通过发布与订阅来自动发现正在监视相同主实例的其他Sentinel，每个 Sentinel 都订阅了被它监视的所有主服务器和从服务器的  \_\_sentinel\_\_:hello 频道， 查找之前未出现过的 sentinel进程。 当一个 Sentinel 发现一个新的 Sentinel 时，它会将新的 Sentinel 添加到一个列表中，这个列表保存了 Sentinel 已知的，监视同一个主服务器的所有其他Sentinel。

注：文中的横杠要替换为下滑线，markdown不太能显示出来...