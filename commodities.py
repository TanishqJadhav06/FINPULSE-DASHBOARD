from config import response
from config import response2
from config import response3
from config import response4

from values import gold_pct
from values import silver_pct
from values import oil_pct



def commodity():
    print("\t  🛢️ 1. COMMODITIES")
    print("----------------------------------------")
    commodities=response.json()

    print("Asset\t\t     Price (USD)  Change")
    print("----------------------------------------")
    print(f"🥇  Gold (XAU/USD)    {commodities["rates"]["XAU"]}    {gold_pct:.2f}%")

    print(f"🥈  Silver (XAG/USD)    {commodities["rates"]["XAG"]}     {silver_pct:.2f}%")

    print(f"🛢️  Crude Oil (WTI)      {commodities["rates"]["WTIOIL-FUT"]}     {oil_pct:.2f}%")


    Naturalgas = response2.json()
    latest = list(Naturalgas["data"])[0]
    print(f"🔥 Natural Gas          {float(latest["value"]):.2f}")


    corn = response3.json()
    latest = list(corn["data"])[0]
    print(f"🌽 Corn (USD/ton)       {float(latest['value']):.2f}")


    Wheat = response4.json()
    latest = list(Wheat["data"])[0]
    print(f"🌾 Wheat (USD/ton)      {(float(latest['value'])):.2f}\n")

commodity()