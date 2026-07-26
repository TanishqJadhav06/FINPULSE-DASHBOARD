

from commodities import commodity

from currencies import currency

from markets import market

from news import news

from Risk import risk
from header import header
from rich.console import Console

console = Console()

def main():
    console.print(header())

if __name__ == "__main__":
    main()

commodity()
currency()
market()
news()
risk()


