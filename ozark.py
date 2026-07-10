import requests
import json
response2 = requests.get(
        "https://www.alphavantage.co/query?function=NATURAL_GAS&interval=monthly&apikey=HTQRWVS672646MI7"
    )
print(json.dumps(response2.json(),indent=2))