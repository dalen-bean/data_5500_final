import requests
import json
import time

x = 0
tickers = ["AAPL", "TSLA", "AMZN", "FB", "GME", "GOOG", "MSFT", "COKE", "PEP", "AMD"]

for ticker in tickers:
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + tickers[x] + '&outputsize=full&apikey=NG9C9EPVBMQTOC8'
    request = requests.get(url)
    req_dict =json.loads(request.text)
    # json.dump(req_dict, open("results.json", "w"))
    time.sleep(12)
    #wait 12 seconds between each ticker
    
    key1 = "Time Series (Daily)"
    key2 = "4. close"
    
    fil = open(ticker + ".csv", "w")
    fil.write("Date, Price\n")
    
    write_lines = []
    for date in req_dict[key1]:
        print(date + ", " + req_dict[key1][date][key2])
        # fil.write(date + ", " + req_dict[key1][date][key2] + "\n")
        write_lines.append(date + ", " + req_dict[key1][date][key2] + "\n")
        
    # write_lines = write_lines[::-1]
    write_lines.reverse()
    fil.writelines(write_lines)
    fil.close()
    x += 1