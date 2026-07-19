from config import currency_response

from percentage import USD_pct
from percentage import EUR_pct
from percentage import JPY_pct
from percentage import GBP_pct
from percentage import CNY_pct
from percentage import AUD_pct


def currency():
    currency=currency_response.json()

    USD_pctn=str(f"{USD_pct:.2f}%")
    EUR_pctn=str(f"{EUR_pct:.2f}%")
    JPY_pctn=str(f"{JPY_pct:.2f}%")
    GBP_pctn=str(f"{GBP_pct:.2f}%")
    CNY_pctn=str(f"{CNY_pct:.2f}%")
    AUD_pctn=str(f"{AUD_pct:.2f}%")


    usdrate=str(f"{(currency["rates"]["INR"]):.2f}")
    Eurorate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["EUR"])):.2f}")
    JPYrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["JPY"])):.2f}")
    GBPrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["GBP"])):.2f}")
    CNYrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["AUD"])):.2f}")
    AUDrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["CNY"])):.2f}")



    from rich.console import Console
    from rich.table import Table

    table=Table(title="🌐 2. GLOBAL CURRENCIES (vs INR)",style="bold")
    console=Console()

    table.add_column("Pair",style="bold cyan",)
    table.add_column("Price (INR)",style=" bold white")
    table.add_column("Change",style=" bold green")
    table.add_row("$💵  USD/INR",usdrate,USD_pctn)
    table.add_row("€💶  EUR/INR",Eurorate,EUR_pctn)
    table.add_row("Ұ💴  JPY/INR",JPYrate,JPY_pctn)
    table.add_row("£💷  GBP/INR",GBPrate,GBP_pctn)
    table.add_row("¥💴  CNY/INR",CNYrate,CNY_pctn)
    table.add_row("$💵  AUD/INR",AUDrate,AUD_pctn)
    print(f"Last Updated🕒: {currency["date"]}\n")

    console.print(table)
if __name__=="__main__":
    currency()