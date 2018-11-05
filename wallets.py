
#wallets = {'EX001': {'BTC': 1, 'ETH': 0, 'XRP': 15}}
wallets = {}


class wallet():
    tradeamount = 0.99    # it cost 1% of amount for every trade

    def __init__(self, experiment, crypto_name, balance):
        self.experiment = experiment
        self.crypto_name = crypto_name
        self.balance = balance
        if experiment in wallets:
            wallets[self.experiment].append((self.crypto_name, self.balance))
        else:
            wallets[self.experiment] = [(self.crypto_name, self.balance)]

    def sell(self, amount):
        self.amount = amount
        self.balance = self.balance - (amount * tradeamount)

    def buy(self, amount):
        self.amount = amount
        self.balance = self.balance + (amount * tradeamount)


def balance(experiment):
    for experiment in wallets:
        print(wallets[experiment])
