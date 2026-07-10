
from config import response
from config import response_lol


change=response_lol.json()
today=response.json()

gold_pct = ((today["rates"]["XAU"] - float(change["rates"]["XAU"]["close"])) / float(change["rates"]["XAU"]["close"])) * 100
silver_pct = ((today["rates"]["XAG"] - float(change["rates"]["XAG"]["close"])) / float(change["rates"]["XAG"]["close"])) * 100
oil_pct = ((today["rates"]["WTIOIL-FUT"] - float(change["rates"]["WTIOIL-FUT"]["close"])) / float(change["rates"]["WTIOIL-FUT"]["close"])) * 100

