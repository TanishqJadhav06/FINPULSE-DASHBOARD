import requests

import json


date=input("Enter date :")
# this api consists (format YYYY-MM-DD)
response = requests.get(
    "https://api.commoditypriceapi.com/v2/rates/historical",
    params={f"symbols": "xau,xag,wtioil-fut", "date": {date}},
    headers={"x-api-key": "572d1cae-cd24-4b3f-b2f5-68a626018afd"},
)

yesterday_change=response.json()
print(json.dumps(response.json(),indent=2))
print(f"Yesterday's Close Gold:{yesterday_change["XAU"]["close"]}")
print(f"Yesterday's Close Sliver{yesterday_change["XAG"]["close"]}")
print(f"Yesterday's Close Oil(WTI){yesterday_change["WTIOIL-FUT"]["close"]}")