from Htests import *
from wallets import *

exp = Htest(5, 'BTC', 'ETH')
exp.currenthour()

exp = Htest(15, 'BTC', 'ETH')
exp.graph()

balance('EX001')
