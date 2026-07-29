from config import response
from config import resonpse_gas
from config import response3
from config import response4

from values import naturalgas_pct
from values import gold_pct
from values import silver_pct
from values import oil_pct

def fmt_pct(pct):
    color = "green" if pct >= 0 else "red"
    arrow = "▲" if pct >= 0 else "▼"
    return f"[{color}]{arrow} {pct:+.2f}%[/{color}]"


def commodity():
    commodities=response.json()


    data=resonpse_gas.json()
    latest = data["data"][0]

    Wheat = response4.json()
    latestwheat = list(Wheat["data"])[0]

    corn = response3.json()
    latestcorn = list(corn["data"])[0]


    gold_pctn=(fmt_pct(gold_pct))
    silver_pctn=(fmt_pct(silver_pct))
    oil_pctn=(fmt_pct(oil_pct))
    naturalgas_pctn=(fmt_pct(naturalgas_pct))

    from rich.console import Console
    from rich.table import Table
    from rich import box
    from rich.panel import Panel
    from rich.text import Text
    content=Text()
    table=Table(title="🛢️  1. COMMODITIES",style="white",title_justify="center")
    console=Console()

    table.add_column("Global Asset",style="bold cyan",justify="left")
    table.add_column("Price (USD)",style="bold white",justify="right")
    table.add_column("Change",style="bold green",justify="right")

    table.add_row("🥇 Gold (XAU/USD)",f"{(commodities["rates"]["XAU"]):,.2f}",gold_pctn)

    table.add_row("🥈 Silver (XAG/USD)",f"{(commodities["rates"]["XAG"]):,.2f}",silver_pctn)

    table.add_row("⛽ Crude Oil (WTI)",f"{(commodities["rates"]["WTIOIL-FUT"]):,.2f}",oil_pctn)

    table.add_row("🔥 Natural Gas",f"{(latest["value"]):,.2f}",naturalgas_pctn)

    table.add_row("🌽 Corn (USD/ton)",f"{float(latestwheat['value']):,.2f}","N/A")

    table.add_row(f"🌾 Wheat (USD/ton)",f"{float(latestcorn['value']):,.2f}","N/A")

    console.print(table)

if __name__=="__main__":
    commodity()