import alpaca_trade_api as trading_api
import json
import requests
import append_data
import time

    
append_data.append_data()

def simplemovingaverage(prices):
    i = 0
    buy = 0
    sell = 0
    position = 0
    tot_profit = 0

    for price in prices:
        if i >= 5:
            avrage = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
            if price > avrage and position != 1:
                
                buy = price
                position = 1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("SM", ticker, "Buy today at:", buy)
                        buy_order
                        time.sleep(5)
                    tot_profit += sell - buy
                    
            elif price < avrage and position != -1:
                sell = price
                position = -1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("SM", ticker, "Sell today at:", sell)
                        sell_order
                        time.sleep(5)
                    tot_profit += sell - buy
                    
            else:
                pass
            
        i += 1
        tot_profit = round(tot_profit,2)
    print("SM", ticker, "Total profit: ", tot_profit)
    return round((tot_profit),2), round(tot_profit / prices[0],2)
    
def meanreversion(prices):
    i = 0
    buy = 0
    sell = 0
    position = 0
    tot_profit = 0
    
    for price in prices:
        if i >= 5:
            avrage = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
            if price < avrage*.95 and position != 1:
                
                buy = price
                position = 1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("MR", ticker, "Buy today at:", buy)
                        buy_order
                        time.sleep(5)
                    tot_profit += sell - buy
                    
            elif price > avrage*1.05 and position != -1:
                sell = price
                position = -1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("MR",ticker, "Sell today at:", sell)
                        sell_order
                        time.sleep(5)
                    tot_profit += sell - buy
            else:
                pass
                
        i += 1
        tot_profit = round(tot_profit,2)
    print("MR", ticker, "Total profit: ", tot_profit)
    return round((tot_profit),2), round(tot_profit / prices[0],2)
    
    
def bollingerband(prices):
    i = 0
    buy = 0
    sell = 0
    position = 0
    tot_profit = 0

    for price in prices:
        if i >= 5:
            avrage = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
            if price > avrage*.95 and position != 1:
                
                buy = price
                position = 1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("BB", ticker, "Buy today at:", buy)
                        buy_order
                        time.sleep(5)
                    tot_profit += sell - buy
                   
            elif price < avrage*1.05 and position != -1:
                sell = price
                position = -1
                if buy == 0 and sell == 0:
                    pass
                else:
                    if i == len(prices) -1:
                        print("BB", ticker, "Sell today at:", sell)
                        sell_order
                        time.sleep(5)
                    tot_profit += sell - buy
                    
            else:
                pass
                
        i += 1
        tot_profit = round(tot_profit,2)
    print("BB", ticker, "Total profit: ", tot_profit)
    return round((tot_profit),2), round(tot_profit / prices[0],2)

print("-------------------------------------------")
print("Strategy, Ticker, Buy/Sell, Price")
print("-------------------------------------------")
most_profit = 0
results = {}
tickers = ["AAPL", "TSLA", "AMZN", "FB", "GME", "GOOG", "MSFT", "COKE", "PEP", "AMD"]

for ticker in tickers:
    prices = []
    for line in open("/home/ubuntu/environment/" + ticker + ".csv").readlines()[1:]:
        prices.append(float(line.split(",")[1]))
        
    # Alpaca Variables:
    api_key = "PKL8AWJQASCYRCO26IIE"
    secret_key = "K8HpjcTykGs5dkYzZOs5uJK3G2Ww84e2T6EXU1B9"
    end_point = "https://paper-api.alpaca.markets"
    
    api = trading_api.REST(api_key, secret_key, end_point)
    account = api.get_account()
    
    buy_order = api.submit_order(symbol = ticker, qty = "10", side = "buy", type="market", time_in_force="gtc" )
    sell_order = api.submit_order(symbol = ticker, qty = "10", side = "sell", type="market", time_in_force="gtc" )
    
    
    # Get the results
    profit, returns = meanreversion(prices)
    results[ticker + " mr_profit"] = profit
    results[ticker + " mr_returns"] = returns
    
    profit, returns = simplemovingaverage(prices)
    results[ticker + " sm_profit"] = profit
    results[ticker + " sm_returns"] = returns
    
    profit, returns = bollingerband(prices)
    results[ticker + " bb_profit"] = profit
    results[ticker + " bb_returns"] = returns

print("--------------------------------")

#Find the most profitable stock and trading strategy
print("The most profitable stock was", max(results, key=results.get)) 

print("--------------------------------")
#Save the results as a JSON file   
json.dump(results, open("results.json", "w"))

print(account)
#Set up crontab "crontab -e" edit or create a file

# m h dom mon dow command
# dow = 1-5
#  h = 7
#  m 45

# Example:
# m h dom mon dow command
#   45 07 * * 1-5 /home/ubuntu/enviornment
