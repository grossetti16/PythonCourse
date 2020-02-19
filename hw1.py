import random 

pricelist = {}

class Portfolio:
     def __init__(self):
        self.cash = 0
        self.stocks = {}
        self.mfunds = {}
        self.transhistory = ["TRANSACTION HISTORY"]  #transaction history
    
    
     def history(self): 
        print ("")
        print ("History")
        print(*self.transhistory,sep="\n")

     def printPortfolio(self): 
        print("Assets")
        print("Cash Balance: ",str("{:.2f}".format(self.cash)))
        print("Stocks: ")
        print(self.stocks)
        print("Mutual Funds: ")
        print(self.mfunds)

     def __str__(self): # printing the portfolio
        return str(self.printPortfolio())

        
     def addCash (self,value): # adding Cash to portfolio
        self.value = value 
        self.cash = self.cash + value
        self.transhistory.append(str("{:.2f}".format(value)) + " cash added \nCash Balance: " + str("{:.2f}".format(self.cash))  ) # update transaction list
        
        
     def withdrawCash (self, value): #Withdrawing Cash from protfolio
        self.value = value
        if (value <= 0):
            print( " Warning - No Cash") #With no cash withdraws cannot be made
        if (self.cash < value):
            print("Insufficient Funds")
        self.cash = self.cash - value #New cash value after withdraw
        self.transhistory.append(str("{:.2f}".format(value)) + " cash withdrawn \nCash Balance: " + str("{:.2f}".format(self.cash))  )  # update transaction list
        
        
     def buyStock (self, shares, ticker):# buy stock function
        self.shares = shares
        self.ticker = ticker
        price = pricelist[ticker.ticker]
        value = shares*price 
        self.transhistory.append(str(shares) + " Stock "+str(self.ticker.ticker) +"  bought at " + str("{:.2f}".format(price)) + " a share") #update transaction list 
        self.withdrawCash(value) # uses the withdraw function to withdraw the value
        self.stocks[ticker.ticker] = shares
       
        
     def sellStock (self, ticker, shares): # sell stock function
        self.shares = shares
        self.ticker = ticker
        factor = random.uniform(0.5, 1.5)
        price = pricelist[ticker]
        price = price*factor
        self.transhistory.append(str(shares) + " Stock "+str(self.ticker) +" sold at " + str("{:.2f}".format(price)) + " a share") # adds the transaction to th
        self.addCash(shares*price)
        
     
     def buyMutualFund (self, shares, ticker): #defining the buy mutualfund function
        self.ticker = ticker
        self.shares = shares
        price = 1 # transaction value
        self.transhistory.append(str(shares) + " Mutual Fund "+str(self.ticker.ticker) +"  bought at " + str("{:.2f}".format(price)) + " a share")# adds the transaction to the history
        self.withdrawCash (price*shares) #cash amount withdrawn for mutualfund transaction
        self.mfunds[ticker.ticker] = shares
        
     def sellMutualFund (self, ticker, shares): # #defining the sell mutualfund function
        self.ticker = ticker
        self.shares = shares
        price = round(random.uniform(0.9,1.2)) #takes out random factor for price change between .9 and 1.2
        self.transhistory.append(str(shares) + " Mutual Fund "+str(self.ticker) +" sold at " + str("{:.2f}".format(price)) + " a share") # updates ttransactions
        self.addCash(shares*price)#value of transaction
        
class MutualFund: # defining Mutual Fund
     def __init__(self, ticker):
        self.ticker = ticker
        

class Stock: # defining stock
     def __init__(self, price, ticker):
        self.ticker = ticker
        self.price = price
        pricelist[ticker] = price # Has a list in which the price is determined and specified by the ticker
    
    
        
if __name__ == '__main__': #Add this if you want to run the test with this script.
    portfolio = Portfolio()              # create a new portfolio
    portfolio.addCash(300.50)            # add cash to the portfolio
    s = Stock(price=20, ticker="HFH")    # create a stock HFH
    portfolio.buyStock(5, s)             # buy 5 shares of stock s
    mf1 = MutualFund("BRT")              # create MF BRT
    mf2 = MutualFund("GHT")              # create MF GHT
    portfolio.buyMutualFund(10.3, mf1)   # Buy 10.3 shares of BRT
    portfolio.buyMutualFund(2, mf2)      # Buy 2 shares of GHT
    portfolio.printPortfolio()          # print portfolio
    portfolio.sellMutualFund("BRT", 3)   # Sell 3 shares of BRT
    portfolio.sellStock("HFH", 1)        # Sell 1 share of HFH
    portfolio.withdrawCash(50)           # Withdraw 50
    portfolio.addCash(19.80)             #add cash  add cash to the portfolio
    portfolio.history()                  # Show a transaction history ordered by time
        
        
        
        
        
            
            