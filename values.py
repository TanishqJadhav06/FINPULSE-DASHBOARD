
from config import response
from config import response_lol

from config import resonpse_oil


change=response_lol.json()
today=response.json()

gold_pct = ((today["rates"]["XAU"] - float(change["rates"]["XAU"]["close"])) / float(change["rates"]["XAU"]["close"])) * 100
silver_pct = ((today["rates"]["XAG"] - float(change["rates"]["XAG"]["close"])) / float(change["rates"]["XAG"]["close"])) * 100
oil_pct = ((today["rates"]["WTIOIL-FUT"] - float(change["rates"]["WTIOIL-FUT"]["close"])) / float(change["rates"]["WTIOIL-FUT"]["close"])) * 100



data=resonpse_oil.json()
latest = data["data"][0]
second_latest = data["data"][1]

naturalgas_pct=((latest["value"] - float(second_latest["value"])) /float(second_latest["value"]))*100

print(gold_pct)