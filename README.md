This project was created with the intention 

This program reads a text file containing stock ticker symbols on each line

Ticker symbols are placed in a list

List is iterated through, gathering data on the 50 and 200 day moving average of each stock (using yfinance python package)

If the 50 day moving average exceeds the 200 day moving average, the stock is added to a buy list

The stock is added to a sell list if the opposite is true

The results of the analysis are written to a text file called "actions.txt" 

This file contains the stock ticker symbols from the original text file, split into buys and sells
