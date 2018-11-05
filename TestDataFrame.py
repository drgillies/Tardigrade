from Htests import *
from wallets import *

#exp = Htest(5, 'BTC', 'ETH')
# exp.currenthour()

#exp = Htest(15, 'BTC', 'ETH')
# xp.graph()

ex001 = wallet('ex001')
ex002 = wallet('ex002')

ex001.addbalance('BTC', 5)
ex002.addbalance('ETH', 10)
ex002.addbalance('BTC', 238)

# balance('EX001')
print(wallets)
