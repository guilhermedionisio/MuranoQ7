import functions
import os
import pandas as pd
import matplotlib.pyplot as plt

stocksPath = "Stocks"
chosenStocks = ["amd", "intc", "aapl", "msft", "nvda",
               "tsm", "orcl", "asml", "avgo", "googl"]

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

if __name__ == "__main__":
    itemA()

