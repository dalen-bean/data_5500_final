import alpaca_trade_api as trading_api
import json
import requests

#Set up crontab "crontab -e"
# Look at append function to make sure it's working right

api_key = "PKP1YA5XNP9FBW9JNTBC"
secret_key = "fVrBkaeTNMMVjVZ6RhOBtoeBct2xSafeWz01Kn2W"
end_point = "https://paper-api.alpaca.markets"

api = trading_api.REST(api_key, secret_key, end_point, api_version="v2")

account = api.get_account()

print(account)
