

from commodities import commodity

from currencies import currency

from markets import market

from news import news

from Risk import risk
from header import header
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    console.print(header())
    row1 = Table.grid(expand=True)
    row1.add_column(ratio=1)
    row1.add_column(ratio=1)
    row1.add_column(ratio=1)
    row1.add_row(commodity(), currency(),market())

    row2 = Table.grid(expand=True)
    row2.add_column(ratio=1)
    row2.add_column(ratio=1)
    row2.add_row(risk(), news())

    console.print(row1)
    console.print(row2)
if __name__ == "__main__":
    main()


