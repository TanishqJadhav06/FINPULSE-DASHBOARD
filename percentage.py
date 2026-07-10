from config import response_tell
from config import currency_response


latest=currency_response.json()
notlatest=response_tell.json()

USD_pct = ((latest["rates"]["INR"] - float(notlatest["rates"]["INR"])) / float(notlatest["rates"]["INR"])) * 100
EUR_pct = ((latest["rates"]["EUR"] - float(notlatest["rates"]["EUR"])) / float(notlatest["rates"]["EUR"])) * 100
JPY_pct = ((latest["rates"]["JPY"] - float(notlatest["rates"]["JPY"])) / float(notlatest["rates"]["JPY"])) * 100
GBP_pct = ((latest["rates"]["GBP"] - float(notlatest["rates"]["GBP"])) / float(notlatest["rates"]["GBP"])) * 100
CNY_pct = ((latest["rates"]["CNY"] - float(notlatest["rates"]["CNY"])) / float(notlatest["rates"]["CNY"])) * 100
AUD_pct = ((latest["rates"]["AUD"] - float(notlatest["rates"]["AUD"])) / float(notlatest["rates"]["AUD"])) * 100
