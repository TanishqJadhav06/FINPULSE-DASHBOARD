import requests
import yfinance as yf
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

#api are stored in a env file for their protection.
COMMODITY_API_KEY = os.getenv("COMMODITY_API_KEY")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
API_TOKEN=os.getenv("API_TOKEN")

#This api get price for GOLD(xau),SILVER(xag) AND CRUDE OIL(wtioil).
response = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/latest",
    params={"symbols": "xau,xag,wtioil-fut"},
    headers={"x-api-key": COMMODITY_API_KEY},
)

# This api gets price of NATURAL GAS (natgas)
resonpse_oil=requests.get(f"https://eodhd.com/api/commodities/historical/NATURAL_GAS?api_token={API_TOKEN}&interval=daily&fmt=json"
)

# This api gets price of CORN.
response3 = requests.get(
    f"https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}"
)
# This api gets price of WHEAT .
response4 = requests.get(
    f"https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}"
)

#This particular api gets price of all currency like USD,INR,EURO,JPY
currency_response = requests.get("https://api.frankfurter.dev/v1/latest?from=USD")


# This api get all the news information
response_news = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWSAPI_KEY}"
)

#This is a library called yfinance which gets live info of Global Indicis
indices = {
    "NIFTY50": "^NSEI", "NASDAQ": "^IXIC", "S&P500": "^GSPC",
    "DOWJONES": "^DJI","BANKNIFTY":"^NSEBANK","SENSEX":"^BSESN",
}


# This get the historical data using dattime libarary which then uses today-1 to make 1 day perctange changes
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





