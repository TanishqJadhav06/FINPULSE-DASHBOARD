from config import response_news
data=response_news.json()


def news():
    from rich.console import Console
    from rich.table import Table
    from rich import box
    console=Console()
    table=Table(title="🗞️  5. News Headlines",box=box.DOUBLE_EDGE,border_style="white")
    table.add_column("📰  TOP MARKET HEADLINES",justify="left")
    for article in data["articles"][1:5]:
        table.add_row(f"● {str(article["title"])}\n")

    return table
if __name__=="__main__":
    news()