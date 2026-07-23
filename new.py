from config import response
from config import resonpse_gas
from config import response3
from config import response4

from values import naturalgas_pct
from values import gold_pct
from values import silver_pct
from values import oil_pct

from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()


def fmt_change(pct):
    """Green/red, signed percentage — e.g. +0.87% / -0.68%"""
    color = "green" if pct >= 0 else "red"
    return f"[{color}]{pct:+.2f}%[/{color}]"




def commodity():
    commodities = response.json()

    data = resonpse_gas.json()
    latest = data["data"][0]

    Wheat = response4.json()
    latestwheat = list(Wheat["data"])[0]

    corn = response3.json()
    latestcorn = list(corn["data"])[0]

    table = Table(show_header=True, header_style="bold white", box=None, padding=(0, 2))

    table.add_column("Asset", justify="left", style="cyan", no_wrap=True)
    table.add_column("Price (USD)", justify="right", style="white")
    table.add_column("Change", justify="right")

    table.add_row(
        "🥇 Gold (XAU/USD)",
        f"{float(commodities['rates']['XAU']):,.2f}",
        fmt_change(gold_pct),
    )
    table.add_row(
        "🥈 Silver (XAG/USD)",
        f"{float(commodities['rates']['XAG']):,.2f}",
        fmt_change(silver_pct),

    )
    table.add_row(
        "🛢️ Crude Oil (WTI)",
        f"{float(commodities['rates']['WTIOIL-FUT']):,.2f}",
        fmt_change(oil_pct),

    )
    table.add_row(
        "🔥 Natural Gas",
        f"{float(latest['value']):,.2f}",
        fmt_change(naturalgas_pct),

    )
    table.add_row(
        "🌽 Corn (USD/bu)",
        f"{float(latestcorn['value']):.2f}",
        "[dim]N/A[/dim]",
        "[dim]— — —[/dim]",
    )
    table.add_row(
        "🌾 Wheat (USD/bu)",
        f"{float(latestwheat['value']):.2f}",
        "[dim]N/A[/dim]",
        "[dim]— — —[/dim]",
    )

    source_line = Text("Source: CommodityAPI", style="blue")

    body = Group(table, Text(""), source_line)

    panel = Panel(
        body,
        title="[yellow]📊  1. COMMODITIES[/yellow]",
        title_align="left",
        border_style="bright_blue",
        padding=(1),
    )
    console.print(panel)


if __name__ == "__main__":
    commodity()