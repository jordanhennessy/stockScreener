The concept of this program is to perform basic stock analysis using data fetched from an external source (Yahoo Finance). 
The program is simple but effective in producing recommendations based on the data it retrieves, then outputting these recommendations to a text file.
Further information on how the program works can be found below:



-Program reads a text file ("portfolio.txt") containing stock ticker symbols on each line

-Ticker symbols are placed in a list

-List is iterated through, gathering data on the 50 and 200 day moving average of each stock (using yfinance python package)

-If the 50 day moving average exceeds the 200 day moving average, the stock is added to a buy list

-The stock is added to a sell list if the opposite is true

-The results of the analysis are written to a text file called "actions.txt" 

-This file contains the stock ticker symbols from the original text file, split into buys and sells
