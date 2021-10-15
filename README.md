This program reads a text file containing stock ticker symbols on each line

ticker symbols are placed in a list

list is iterated through, gathering data on the 50 and 200 day moving average of each stock (using yfinance python package)

if the 50 day moving average exceeds the 200 day moving average, the stock is added to a buy list

the stock is added to a sell list if the opposite is true

the results of the analysis are written to a text file called "actions.txt" 

this file contains the stock ticker symbols from the original text file, split into buys and sells
