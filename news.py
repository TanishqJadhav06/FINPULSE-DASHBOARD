from config import response_news
data=response_news.json()


def news():
    print("\n📰 5. TOP MARKET HEADLINES")
    print("---------------------------")
    for article in data["articles"][4:8]:
        print(f"\n{article["title"]}")
        print(article["description"])
        print("---------")

news()