### INF601 - Advanced Programming in Python
### Corbin Luck
### Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import copy
from pathlib import Path

# Creates the charts folder if one does not exist
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

## List of the stocks wanting to find closing price of
mystocks = ["MSFT", "NVDA", "AAPL", "WMT", "AMC"]
mystockdata= {}

## Creates the list and then the array
for stock in mystocks:
    dat = yf.Ticker(stock)
    last10 = dat.history(period="10d")
    mystockdata[stock] = []
    for price in last10["Close"]:
        mystockdata[stock].append(price)
    mystock = np.array(mystockdata[stock])

## Gets the high and low price from the list
    highlow = copy.copy(mystockdata[stock])
    highlow.sort()

## Creates the graphs
    plt.plot(mystock)
    plt.ylabel('Closing Price')
    plt.xlabel('Trading Days Ago')
    plt.axis((0, 10, highlow[0] - 5, highlow[-1] + 5))
    plt.title('Closing Price for ' + stock)
    plt.savefig(f'charts/{stock}.png')
    plt.show()


