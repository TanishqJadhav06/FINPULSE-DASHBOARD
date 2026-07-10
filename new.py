import requests

response=requests.get("https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey=HTQRWVS672646MI7")
print(response.json())