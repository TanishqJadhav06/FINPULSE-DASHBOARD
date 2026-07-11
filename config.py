import requests
import json
import sys
import emoji
import yfinance as yf
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

COMMODITY_API_KEY = os.getenv("COMMODITY_API_KEY")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
API_TOKEN=os.getenv("API_TOKEN")

response = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/latest",
    params={"symbols": "xau,xag,wtioil-fut"},
    headers={"x-api-key": COMMODITY_API_KEY},
)


resonpse_oil=requests.get(f"https://eodhd.com/api/commodities/historical/NATURAL_GAS?api_token={API_TOKEN}&interval=daily&fmt=json"
)


response3 = requests.get(
    f"https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}"
)

response4 = requests.get(
    f"https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}"
)

currency_response = requests.get("https://api.frankfurter.dev/v1/latest?from=USD")

response_news = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWSAPI_KEY}"
)

indices = {
    "NIFTY50": "^NSEI", "NASDAQ": "^IXIC", "S&P500": "^GSPC",
    "DOWJONES": "^DJI", "BANKNIFTY": "^NSEBANK", "SENSEX": "^BSESN",
}

yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
# this api consists (format YYYY-MM-DD)
response_lol = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/historical",
    params={"symbols": "xau,xag,wtioil-fut", "date": str(yesterday)},
    headers={"x-api-key": COMMODITY_API_KEY},
)

date = datetime.datetime.now().date() - datetime.timedelta(days=2)
# this api consists (format YYYY-MM-DD)
response_tell = requests.get(f"https://api.frankfurter.dev/v1/{date}?from=USD"
)





