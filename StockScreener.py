import yfinance as yf


# open text file containing list of stocks
portfolio = open("portfolio.txt", mode = "r")

# initialise empty list in which to append the stocks
stockList = []

for line in portfolio:
    stockList.append(line.strip())

# create new blank file to write the results of the stock analysis to later
actions = open("actions.txt", "w")

# initialise two empty lists in which to append the stocks based on the decision made
buys = []
sells = []

# iterate through the stocks in the list of stocks
for stock in stockList:
    
    # find the 50 and 200 day moving averages of the stock
    stockShort = yf.Ticker(stock).history(period = '50d')
    stockLong = yf.Ticker(stock).history(period = '200d')
    
    # select the column related to the close price of the stock
    stockShortClose = stockShort["Close"]
    stockLongClose = stockLong["Close"]
    
    # initialise a variable for the total of the close prices across 50 and 200 day periods
    stockShortTotal = 0
    stockLongTotal = 0

    
    # iterate through the close price of the stock across 50 days and add to the total
    for i in stockShortClose:
        stockShortTotal += i

    # iterate through the close price of the stock across 200 days and add to the total
    for i in stockLongClose:
        stockLongTotal += i
    
    # calculate the average for the 50 and 200 day periods 
    stockShortAvg = stockShortTotal/len(stockShortClose)
    stockLongAvg = stockLongTotal/len(stockLongClose)

    
    # makes the decision on whether the stock is added to the buys or sells lists
    if stockShortAvg > stockLongAvg:
        buys.append(stock)
    elif stockShortAvg < stockLongAvg:
        sells.append(stock)

    # prints message to confirm the stock has been successfully read and been assigned to one of the two options
    print("\n" + stock, "successfully screened, action assigned")


    
# the following code is used to format and write the results of the analysis to the text file "actions.txt" which was initialised earlier
actions.write("--- BUYS --- ")

for i in buys:
    actions.write("\n   -")
    actions.write(i)
    
for i in range(0,2):
    actions.write("\n")

actions.write("--- SELLS ---")

for i in sells:
    actions.write("\n   -")
    actions.write(i)


# this gives the user the opportunity to read the confirmation messages before closing the program
input("\n\npress enter to exit")
