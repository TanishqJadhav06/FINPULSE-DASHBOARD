import requests

import json

import sys

import emoji

import yfinance as yf

import datetime

response = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/latest",
    params={"symbols": "xau,xag,wtioil-fut"},
    headers={"x-api-key": "572d1cae-cd24-4b3f-b2f5-68a626018afd"},
)

response2 = requests.get(
        "https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=HTQRWVS672646MI7"
    )

response3 = requests.get(
        "https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey=HTQRWVS672646MI7"
    )

response4 = requests.get(
        "https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=HTQRWVS672646MI7"
    )

currency_response=requests.get("https://api.frankfurter.dev/v1/latest?from=USD"
    )

response_news= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4b407a5e42bb45cdb888d271d184d90f"
    )

indices = {
    "NIFTY50": "^NSEI", "NASDAQ": "^IXIC", "S&P500": "^GSPC",
    "DOWJONES": "^DJI","BANKNIFTY":"^NSEBANK","SENSEX":"^BSESN",
}

yesterday=datetime.datetime.now().date()-datetime.timedelta(days=1)
    # this api consists (format YYYY-MM-DD)
response_lol = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/historical",
    params={f"symbols": "xau,xag,wtioil-fut", "date": {yesterday}},
    headers={"x-api-key": "572d1cae-cd24-4b3f-b2f5-68a626018afd"},
)

date=datetime.datetime.now().date()-datetime.timedelta(days=2)
    # this api consists (format YYYY-MM-DD)
response_tell=requests.get(f"https://api.frankfurter.dev/v1/{date}?from=USD"
    )

