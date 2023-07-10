import os
import pandas as pd
import seaborn as sns
import matplotlib as plt

def movingAverage(data, window):
    close_prices = data['Close']
    ma = close_prices.rolling(window=window).mean()
    return ma

def plotMovingAverage(data, windows, stock, ax):
    ax.set_title(stock)
    ax.set_xlabel('Days')
 
    sns.lineplot(data=data, x=data.index, y='Close', label='Close Prices', ax=ax)

    for window in windows:
        ma = movingAverage(data, window)
        sns.lineplot(data=ma, x=ma.index, y=ma.values, label=f'MA ({window} days)',ax=ax)