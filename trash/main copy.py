import json

import yfinance as yf

from config import response
from config import response2
from config import response3
from config import response4
from config import currency_response
from config import response_news

#<------------------------------------------------------Cmmoditites------------------------------------------------------------------------------>
print("🛢️ 1. COMMODITIES")
print("-------------------------")
commodities=response.json()

print("Asset\t\t     Price (USD)")
print("-------------------------")
print(f"🥇  Gold (XAU/USD)    {commodities["rates"]["XAU"]}")

print(f"🥈  Silver (XAG/USD)    {commodities["rates"]["XAG"]}")

print(f"🛢️  Crude Oil (WTI)      {commodities["rates"]["WTIOIL-FUT"]}")


Naturalgas = response2.json()
latest = list(Naturalgas["data"])[0]
print(f"🔥 Natural Gas          {float(latest["value"]):.2f}")


corn = response3.json()
latest = list(corn["data"])[0]
print(f"🌽 Corn (USD/ton)       {float(latest['value']):.2f}")


Wheat = response4.json()
latest = list(Wheat["data"])[0]
print(f"🌾 Wheat (USD/ton)      {(float(latest['value'])):.2f}\n")

#<------------------------------------------------------Global Currency------------------------------------------------------------------------------>

print("🌐 2. GLOBAL CURRENCIES (vs INR)")
print("--------------------------------")
currency=currency_response.json()

print("Pair \t   Price")
print("---------------")
print(f"USD/INR    {currency["conversion_rates"]["INR"]*(float(currency["conversion_rates"]["USD"])):.2f}")
print(f"EUR/INR    {currency["conversion_rates"]["INR"]/(float(currency["conversion_rates"]["EUR"])):.2f}")
print(f"JPY/INR    {currency["conversion_rates"]["INR"]/(float(currency["conversion_rates"]["JPY"])):.2f}")
print(f"GBP/INR    {currency["conversion_rates"]["INR"]/(float(currency["conversion_rates"]["GBP"])):.2f}")
print(f"CNY/INR    {currency["conversion_rates"]["INR"]/(float(currency["conversion_rates"]["CNY"])):.2f}")
print(f"AUD/INR    {currency["conversion_rates"]["INR"]/(float(currency["conversion_rates"]["AUD"])):.2f}")
print(f"Last Updated🕒: {currency["time_last_update_utc"]}\n")



#<------------------------------------------------------Global Markets------------------------------------------------------------------------------>
print("🗺 3. Global MARKETS")
print("--------------------")
indices = {
    "NIFTY50": "^NSEI", "NASDAQ": "^IXIC", "S&P500": "^GSPC",
    "DOWJONES": "^DJI","BANKNIFTY":"^NSEBANK","SENSEX":"^BSESN",
}
print("Index\t   Value     Change")
print("--------------------------")
for name, symbol in indices.items():
    try:
        t = yf.Ticker(symbol)
        price = t.fast_info["lastPrice"]
        prev = t.fast_info["previousClose"]
        pct = (price - prev) / prev * 100
        print(f"{name:<10} {price:.2f}  {pct:+.2f}%")
    except Exception as e:
        print(f"{name:<10} error: {e}")

#<------------------------------------------------------Global Headlines------------------------------------------------------------------------------>

print("\n📰 5. TOP MARKET HEADLINES")
print("---------------------------")
for article in response_news["articles"][3:9]:
    print(f"\n{article["title"]}")
    print(article["description"])
    print("---------")