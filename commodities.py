from config import response
from config import resonpse_gas
from config import response3
from config import response4

from values import naturalgas_pct
from values import gold_pct
from values import silver_pct
from values import oil_pct

def commodity():
    commodities=response.json()


    data=resonpse_gas.json()
    latest = data["data"][0]

    Wheat = response4.json()
    latestwheat = list(Wheat["data"])[0]

    corn = response3.json()
    latestcorn = list(corn["data"])[0]


    gold_pctn=(f"{gold_pct:.2f}%")
    silver_pctn=(f"{silver_pct:.2f}%")
    oil_pctn=(f"{oil_pct:.2f}%")
    naturalgas_pctn=(f"{naturalgas_pct:.2f}%")

    from rich.console import Console
    from rich.table import Table

    table=Table(title="🛢️  1. COMMODITIES",style="bold",title_justify="center")
    console=Console()

    table.add_column("Asset Price",justify="left",style="cyan")
    table.add_column("Price (USD)",style="white")
    table.add_column("Change",style="green")

    table.add_row("🥇 Gold (XAU/USD)",str(commodities["rates"]["XAU"]),gold_pctn)

    table.add_row("🥈 Silver (XAG/USD)",str(commodities["rates"]["XAG"]),silver_pctn)

    table.add_row("🛢️ Crude Oil",str(commodities["rates"]["WTIOIL-FUT"]),oil_pctn)

    table.add_row("🔥 Natural Gas",str(latest["value"]),naturalgas_pctn)

    table.add_row("🌽 Corn (USD/ton)",f"{float(latestwheat['value']):.2f}","N/A")

    table.add_row(f"🌾 Wheat (USD/ton)",f"{float(latestcorn['value']):.2f}","N/A")

    console.print(table)

if __name__=="__main__":
    commodity()