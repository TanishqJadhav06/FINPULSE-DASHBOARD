from config import currency_response

from percentage import USD_pct
from percentage import EUR_pct
from percentage import JPY_pct
from percentage import GBP_pct
from percentage import CNY_pct
from percentage import AUD_pct


def fmt_pct(pct):
    color = "green" if pct >= 0 else "red"
    arrow = "▲" if pct >= 0 else "▼"
    return f"[{color}]{arrow} {pct:+.2f}%[/{color}]"


def currency():
    currency=currency_response.json()

    USD_pctn=(fmt_pct(USD_pct))
    EUR_pctn=(fmt_pct(EUR_pct))
    JPY_pctn=(fmt_pct(JPY_pct))
    GBP_pctn=(fmt_pct(GBP_pct))
    CNY_pctn=(fmt_pct(CNY_pct))
    AUD_pctn=(fmt_pct(AUD_pct))


    usdrate=str(f"{(currency["rates"]["INR"]):.2f}")
    Eurorate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["EUR"])):.2f}")
    JPYrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["JPY"])):.2f}")
    GBPrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["GBP"])):.2f}")
    CNYrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["AUD"])):.2f}")
    AUDrate=str(f"{currency["rates"]["INR"]/(float(currency["rates"]["CNY"])):.2f}")



    from rich.console import Console
    from rich.table import Table
    from rich import box
    table=Table(title="🌐  2. GLOBAL CURRENCIES (vs INR)",style="white")
    console=Console()

    table.add_column("Pair",style="bold cyan",)
    table.add_column("Price (INR)",style=" bold white",justify="right")
    table.add_column("Change",style=" bold",justify="right")
    table.add_row("$💵  USD/INR",usdrate,USD_pctn)
    table.add_row("€💶  EUR/INR",Eurorate,EUR_pctn)
    table.add_row("Ұ💴  JPY/INR",JPYrate,JPY_pctn)
    table.add_row("£💷  GBP/INR",GBPrate,GBP_pctn)
    table.add_row("¥💴  CNY/INR",CNYrate,CNY_pctn)
    table.add_row("$💵  AUD/INR",AUDrate,AUD_pctn)

    console.print(table)

if __name__=="__main__":
    currency()