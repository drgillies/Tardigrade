from Htests import *
from wallets import *

#exp = Htest(5, 'BTC', 'ETH')
# exp.currenthour()

#exp = Htest(15, 'BTC', 'ETH')
# xp.graph()

wallet('EX001', 'BTC', 5)
wallet('EX001', 'ETH', 4)
wallet('EX002', 'ETH', 3)

balance('EX001')

print(wallets)
