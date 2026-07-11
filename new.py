import requests

API_TOKEN = "6a51e7df476f21.98560786"

def get_commodity(code, interval="daily"):
    url = f"https://eodhd.com/api/commodities/historical/{code}"
    params = {"api_token": API_TOKEN, "interval": interval}
    response = requests.get(url, params=params)
    return response.json()

# Monthly WTI prices
data = get_commodity("WTI")
print(f"Commodity: {data['meta']['name']}")
print(f"Unit: {data['meta']['unit']}")
print(f"Total records: {data['meta']['total']}")

for row1 in data["data"][:1]:
    print(f"  {row1['date']}: ${row1['value']}")

for row2 in data["data"][1:2]:
    print(f"  {row2["date"]}: ${row2['value']}")