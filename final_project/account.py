import alpaca_trade_api as trading_api
import json
import requests

#Set up crontab "crontab -e" edit or create a file

# m h dom mon dow command
# dow = 1-5
#  h = 7
#  m 45

# Example:
# m h dom mon dow command
#   45 07 * * 1-5 /home/ubuntu/enviornment

api_key = "PKMHYTHGY0I962EWIJEX"

secret_key = "lVm0NBCmHXFygDcnpMDRYfFSC1v68qweNJUGHYTr"
end_point = "https://paper-api.alpaca.markets"


api = trading_api.REST(api_key, secret_key, end_point, api_version="v2")

account = api.get_account()

buy_order = api.submit_order(symbol = 'AAPL', qty = "10", side = "buy", type="market", time_in_force="day" )
sell_order = api.submit_order(symbol = 'AAPL', qty = "10", side = "sell", type="market", time_in_force="day" )


print(account)

