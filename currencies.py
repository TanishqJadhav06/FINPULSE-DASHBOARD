from config import currency_response

from percentage import USD_pct
from percentage import EUR_pct
from percentage import JPY_pct
from percentage import GBP_pct
from percentage import CNY_pct
from percentage import AUD_pct
def currency():
    print("🌐 2. GLOBAL CURRENCIES (vs INR)")
    print("---------------------------")
    currency=currency_response.json()

    print("Pair \t   Price     Change")
    print("---------------------------")
    print(f"USD/INR    {currency["rates"]["INR"]}     {USD_pct:.2f}%")
    print(f"EUR/INR    {currency["rates"]["INR"]/(float(currency["rates"]["EUR"])):.2f}    {EUR_pct:.2f}%")
    print(f"JPY/INR    {currency["rates"]["INR"]/(float(currency["rates"]["JPY"])):.2f}      {JPY_pct:.2f}%")
    print(f"GBP/INR    {currency["rates"]["INR"]/(float(currency["rates"]["GBP"])):.2f}    {GBP_pct:.2f}%")
    print(f"CNY/INR    {currency["rates"]["INR"]/(float(currency["rates"]["CNY"])):.2f}     {CNY_pct:.2f}%")
    print(f"AUD/INR    {currency["rates"]["INR"]/(float(currency["rates"]["AUD"])):.2f}     {AUD_pct:.2f}%\n")
    print(f"Last Updated🕒: {currency["date"]}\n")
    
if __name__=="__main__":
    currency()