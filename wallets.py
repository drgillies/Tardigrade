
# wallets = {'EX001': [{'BTC': 1}, {'ETH': 0}, {'XRP': 15}]}
wallets = {}


class wallet():
    tradeamount = 0.99    # it cost 1% of amount for every trade

    def __init__(self, experiment):    # adding a new experiment or balance
        self.experiment = experiment
        wallets[self.experiment] = []

    def addbalance(self, crypto, amount):
        wallets[self.experiment].append({crypto: amount})

    def trade(self, )


def balance(experiment):
    for experiment in wallets:
        print(wallets[experiment])
