
import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
import datetime


class Htest():
    url_hour = 'https://min-api.cryptocompare.com/data/histohour'    # Hourly data
    url_price = 'https://min-api.cryptocompare.com/data/price'       # Current price data
    date = str(datetime.datetime.now())                              # Current date

    def __init__(self, tlen, buy, sell):
        self.tlen = tlen * 24                     # *24 for the amount of hours in a day, tlen = '_' days
        self.buy = buy
        self.sell = sell

    def currenthour(self):
        params = {                            # The pramatars that are reguired to send to the website
            "tryConversion": "False",
            "fsym": str(self.buy),            # What crypto buying
            "tsym": str(self.sell),           # What crypto or currency selling
            "aggregate": 1,                   # Periods
            "limit": self.tlen}               # Amount of days back into history
        r = requests.post(Htest.url_hour, params=params)
        x = r.json()
        df = pd.DataFrame(x['Data'])

        return(df)

    def graph(self):                              # Produces a set graph
        df = self.currenthour()                   # Uses previos part to access data

        # Data for volume at bottom of graph
        nvol_mean = df['volumefrom'].mean()
        df['vol_mean'] = df.rolling(window=50)['volumefrom'].mean()
        df['vol_sd'] = df.rolling(window=50)['volumefrom'].std()
        df['hi_sd'] = df['vol_mean'] + df['vol_sd']
        df['low_sd'] = df['vol_mean'] - df['vol_sd']

        # Data of moving averages
        df['MA24'] = df.rolling(window=24)['close'].mean()
        df['MA12'] = df.rolling(window=12)['close'].mean()
        df['MA36'] = df.rolling(window=36)['close'].mean()

        # Data for bolinger bands
        df['MEAN12'] = df.rolling(window=12)['close'].mean()
        df['ST12'] = df.rolling(window=12)['close'].std()
        df['MPS'] = df['MEAN12'] + (df['ST12'] * 2)
        df['MMS'] = df['MEAN12'] - (df['ST12'] * 2)

        # Plotting
        plt.subplots(figsize=(40, 17))
        df['close'].plot(color='k')
        df['MA12'].plot(color='gold')
        df['MA36'].plot(color='b')
        # df['MEAN12'].plot(color='red')
        # df['MPS'].plot(color='salmon')
        # df['MMS'].plot(color='salmon')
        df['volumefrom'].plot(secondary_y=True, kind='bar', color='blue',
                              )            # Volume plotting
        df['vol_mean'].plot(secondary_y=True, color='red', linewidth=1)
        df['hi_sd'].plot(secondary_y=True, color='salmon', linewidth=.5)
        df['low_sd'].plot(secondary_y=True, color='salmon', linewidth=.5)
        plt.title(str(self.buy) + ' ' + str(self.sell) + ' ' + self.date, fontsize=30)
        plt.ylim(0, (nvol_mean * 10))
        df = plt.show()

        return(df)
