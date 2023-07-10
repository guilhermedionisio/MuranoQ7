import os
import pandas as pd
import seaborn as sns

# ----------------- ITEM A ---------------------- #
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

# ----------------- ITEM B ---------------------- #

def calculateCorrelations(stocksPath):
    stocksNames = os.listdir(stocksPath)
    stocksNames = stocksNames[100:200]
    numStocks = len(stocksNames)
    correlations = {}
    emptyFiles = []

    for i in range(numStocks):
        stockAPath = os.path.join(stocksPath, stocksNames[i])
        try:
            stockAData = pd.read_csv(stockAPath, index_col='Date', usecols=['Date', 'Close'])
        except pd.errors.EmptyDataError:
            if stockAPath not in emptyFiles:
                emptyFiles.append(stockAPath)
                print(f"File {stockAPath} is empty.")
            continue

        for j in range(i+1, numStocks):
            stockBPath = os.path.join(stocksPath, stocksNames[j])
            try:
                stockBData = pd.read_csv(stockBPath, index_col='Date', usecols=['Date', 'Close'])
            except pd.errors.EmptyDataError:
                if stockBPath not in emptyFiles:
                    emptyFiles.append(stockBPath)
                    print(f"File {stockBPath} is empty.")
                continue

            merged_data = pd.merge(stockAData, stockBData, on='Date', suffixes=('_A', '_B'))
            correlation = merged_data['Close_A'].corr(merged_data['Close_B'])
            correlations[(stocksNames[i], stocksNames[j])] = correlation

    return correlations

def sortCorrelations(correlations):
    sortedCorrelations = sorted(correlations.items(), key=getCorrelation)
    return sortedCorrelations

def getCorrelation(pair):
    return pair[1]

def topCorrelations(correlations, numPairs):
    sortedCorrelations = sortCorrelations(correlations)
    topCorrelations = sortedCorrelations[-numPairs:][::-1]

    return topCorrelations

def bottomCorrelations(correlations, numPairs):
    sortedCorrelations = sortCorrelations(correlations)
    bottomCorrelations = sortedCorrelations[:numPairs]

    return bottomCorrelations
