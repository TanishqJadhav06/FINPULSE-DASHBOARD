import requests


response_news= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=4b407a5e42bb45cdb888d271d184d90f"
    )

data = response_news.json()

for article in data["articles"][3:9]:
    print(f"\n{article["title"]}")
    print(article["description"])
    print("---------")