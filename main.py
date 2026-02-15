### INF601 - Advanced Programming in Python
### Corbin Luck
### Mini Project 1


# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

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


