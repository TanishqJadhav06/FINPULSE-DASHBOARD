import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_TOKEN=os.getenv("API_TOKEN")
resonpse_oil=requests.get(f"https://eodhd.com/api/commodities/historical/NATURAL_GAS?api_token={API_TOKEN}&interval=daily&fmt=json"
)
print(resonpse_oil)
