from config import response_news
data=response_news.json()


def news():
    from rich.console import Console
    from rich.table import Table
    from rich import box
    console=Console()
    table=Table(title="News",box=box.DOUBLE_EDGE,border_style="bright_blue")
    table.add_column("📰  5. TOP MARKET HEADLINES",justify="center")
    for article in data["articles"][2:5]:
        table.add_row(f"{str(article["title"])}\n")
    console.print(table)
if __name__=="__main__":
    news()