from config import response

from values import gold_pct
from values import silver_pct
from values import oil_pct

gold_pctn=(f"{gold_pct:.2f}%")
silver_pctn=(f"{silver_pct:.2f}%")
oil_pctn=(f"{oil_pct:.2f}%")

from time import time
from rich.console import Console
from rich.table import Table

table=Table(title="sample table")
console=Console()

table.add_column("🛢️ 1. COMMODITIES",justify="right")
print("----------------------------------------")
commodities=response.json()

table.add_column("Asset Price",justify="right",style="cyan")
table.add_column("Price (USD)",style="white")
table.add_column("Change",style="green")
table.add_row("🥇  Gold (XAU/USD)",{commodities["rates"]["XAU"]} ,{gold_pctn})

table.add_row("🥈  Silver (XAG/USD)",{commodities["rates"]["XAG"]},{silver_pctn})

table.add_row("🛢️  Crude Oil (WTI)",{commodities["rates"]["WTIOIL-FUT"]},{oil_pctn})

console.print(table)