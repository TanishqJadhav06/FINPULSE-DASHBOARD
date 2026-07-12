from values import  gold_pct 
from values import silver_pct
from values import oil_pct
from values import naturalgas_pct

from percentage import USD_pct
from percentage import EUR_pct
from percentage import JPY_pct
from percentage import GBP_pct
from percentage import CNY_pct
from percentage import AUD_pct

from markets import nifty_pct
from markets import nasdaq_pct
from markets import sp500_pct
from markets import dowj_pct
from markets import banknifty_pct
from markets import sensex_pct


score=0

reasons=[]
if gold_pct>1.5:
    score+=-3*3
    reasons.append("Gold is rising!")
elif gold_pct >0.5 and gold_pct <=1.5:
    score+=-2*3
    reasons.append("Gold is rising!")
elif gold_pct >-0.5 and gold_pct <0.5:
    score+=0*3
    reasons.append("Gold is rising!")
elif gold_pct >-1.5 and gold_pct <=-0.5:
    score+=2*3
    reasons.append("Gold is rising!")
else:
    score+=3*3
    reasons.append("Gold is rising!")

print(f"Score:{score}")
print(f"Reasons: {reasons}")