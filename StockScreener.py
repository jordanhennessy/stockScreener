import yfinance as yf

portfolio = open("portfolio.txt", mode = "r")

stockList =[]

for line in portfolio:
    stockList.append(line.strip())



actions = open("actions.txt", "w")

buys = []
sells = []


for stock in stockList:
    stockShort = yf.Ticker(stock).history(period = '50d')
    stockLong = yf.Ticker(stock).history(period = '200d')

    stockShortClose = stockShort["Close"]
    stockLongClose = stockLong["Close"]

    stockShortTotal = 0
    stockLongTotal = 0

    for i in stockShortClose:
        stockShortTotal += i

    for i in stockLongClose:
        stockLongTotal += i


    stockShortAvg = stockShortTotal/len(stockShortClose)
    stockLongAvg = stockLongTotal/len(stockLongClose)

    if stockShortAvg > stockLongAvg:
        buys.append(stock)
    elif stockShortAvg < stockLongAvg:
        sells.append(stock)

    print("\n" + stock, "successfully screened, action assigned")


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


input("\n\npress enter to exit")
