from config import response_news
data=response_news.json()

from rich.console import Console
console=Console()
def news():
    console.print("\n📰 5. TOP MARKET HEADLINES",style="bold purple")
    print("---------------------------")
    for article in data["articles"][4:8]:
        print(f"\n{article["title"]}")
        print(article["description"])
        print("---------")
if __name__=="__main__":
    news()