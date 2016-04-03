#11.1.4.12	Master hang死测试
由于我们的sentinel down-after-milliseconds为3100，即3.1s，因此在master上执行：
debug sleep 3.0，系统不会切换，但是执行debug sleep 3.7或者更大的数值，系统就会判定为主sdown，进而变为odown随后发起投票切换。很难模拟取消odown的，因为时间差很短。
