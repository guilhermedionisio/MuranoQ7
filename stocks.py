import functions
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

stocksPath = "Stocks"
chosenStocks = ["amd", "intc", "aapl", "msft", "nvda",
               "tsm", "orcl", "asml", "avgo", "googl"]
predictStocks = ['goog', 'googl', 'aapl', 'msft']

def itemA():
    movingAverageWindows = [10, 20, 50, 200]
    _, axs = plt.subplots(5, 2, figsize=(16, 10), dpi=150)
    axs = axs.flatten()

    if not os.path.exists("results"):
        os.makedirs("results")

    for i, stock in enumerate(chosenStocks):
        stockPath = functions.os.path.join(stocksPath, stock+".us.txt")
        stockData = pd.read_csv(stockPath)
        functions.plotMovingAverage(stockData, movingAverageWindows, stock, axs[i])
    
    save_path = os.path.join("results", "itemA.png")

    plt.savefig(save_path)

    plt.close()

def itemB():
    correlations = functions.calculateCorrelations(stocksPath)
    top = functions.topCorrelations(correlations, 5)
    bottom = functions.bottomCorrelations(correlations, 5)

    print("Top correlations:")
    for pair, correlation in top:
        stockA, stockB = pair
        print(f"{stockA.split('.')[0]} - {stockB.split('.')[0]}: Correlation = {correlation}")

    print("\nBottom correlations:")
    for pair, correlation in bottom:
        stockA, stockB = pair
        print(f"{stockA.split('.')[0]} - {stockA.split('.')[0]}: Correlation = {correlation}")

def itemC():
    _, axs = plt.subplots(2, 2, figsize=(16, 10), dpi=150)
    axs = axs.flatten()

    for i, stock in enumerate(predictStocks):
        stockPath = os.path.join(stocksPath,  stock + '.us.txt')
        df = pd.read_csv(stockPath, index_col='Date', parse_dates=['Date'])

        df = df[['Close']]

        x = df.dropna().index.values.astype(float).reshape(-1, 1)
        y = df.dropna()['Close'].values

        xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=888)

        model = LinearRegression()

        model.fit(xTrain, yTrain)

        yPred = model.predict(xTest)
        mse = mean_squared_error(yTest, yPred)

        axs[i].scatter(xTest, yTest, color='green', label='Test')
        axs[i].plot(xTest, yPred, color='red', label='Prediction')
        axs[i].set_title(f"Stock Price Prediction for {stock}")
        axs[i].set_xlabel("Date")
        axs[i].set_ylabel("Closing Price")
        axs[i].legend()

        print(f"MSE for {stock}: {mse:.2f}")
    
    save_path = os.path.join("results", "itemC.png")

    plt.savefig(save_path)

    plt.close()

if __name__ == "__main__":
    itemC()


