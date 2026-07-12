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


score=0

reasons=[]

if gold_pct>1.5:
    score+=-3*3
    reasons.append("🟢 Gold strongly supports Risk ON. Safe-haven demand is falling, indicating strong investor confidence.")
elif gold_pct >0.5 and gold_pct <=1.5:
    score+=-2*3
    reasons.append("🟢 Gold supports Risk ON. Investors are gradually moving away from defensive assets")
elif gold_pct >-0.5 and gold_pct <0.5:
    score+=0*3
    reasons.append("⚪ Gold is neutral. No meaningful safe-haven signal today.")
elif gold_pct >-1.5 and gold_pct <=-0.5:
    score+=2*3
    reasons.append("🔴 Gold supports Risk OFF. Investors are showing increased demand for safe-haven assets.")
elif gold_pct<-1.5:
    score+=3*3
    reasons.append("🔴 Gold strongly supports Risk OFF. Strong flight to safety suggests elevated market fear.")
else:
    print("Error getting value form gold")

if silver_pct>1.5:
    score+=-3*1
    reasons.append("🟢 Silver supports economic optimism")
elif silver_pct >0.5 and silver_pct <=1.5:
    score+=-2*1
    reasons.append("🟢 Silver shows improving industrial demand.")
elif silver_pct >-0.5 and silver_pct <0.5:
    score+=0*1
    reasons.append("⚪ Silver is neutral today.")
elif silver_pct >-1.5 and silver_pct <=-0.5:
    score+=2*1
    reasons.append("🔴 Silver reflects weakening industrial demand.")
elif silver_pct<-1.5:
    score+=3*1
    reasons.append("🔴 Silver supports a defensive market tone.")
else:
    print("Error getting value form silver")


if oil_pct>1.5:
    score+=-2*2
    reasons.append("🔴 Rising oil prices increase inflation concerns.")
elif oil_pct >0.5 and oil_pct <=1.5:
    score+=-1*2
    reasons.append("🔴 Oil is slightly inflationary.")
elif oil_pct >-0.5 and oil_pct <0.5:
    score+=0*2
    reasons.append("⚪ Oil is stable today.")
elif oil_pct >-1.5 and oil_pct <=-0.5:
    score+=1*2
    reasons.append("🟢 Lower oil eases inflation pressure.")
elif oil_pct<-1.5:
    score+=2*2
    reasons.append("🟢 Falling oil supports Risk ON through lower inflation.")
else:
    print("Error getting value form oil")


if naturalgas_pct>1.5:
    score+=-1*1
    reasons.append("🔴 Natural gas prices suggest rising energy costs.")
elif naturalgas_pct >0.5 and naturalgas_pct <=1.5:
    score+=-0.5*1
    reasons.append("🔴 Gas prices remain inflationary.")
elif naturalgas_pct >-0.5 and naturalgas_pct <0.5:
    score+=0*2
    reasons.append("⚪ Natural gas is stable.")
elif naturalgas_pct >-1.5 and naturalgas_pct <=-0.5:
    score+=0.5*1
    reasons.append("🟢 Lower gas prices reduce energy cost pressure.")
elif naturalgas_pct<=-1.5:
    score+=1*1
    reasons.append("🟢 Falling gas supports improving inflation expectations.")
else:
    print("Error getting value form Natural Gas")


if USD_pct >1.5:
    score+=-3*3
    reasons.append("🔴 Stronger USD reflects global demand for safety.")
elif USD_pct>0.5 and USD_pct <=1.5:
    score+=-2*3
    reasons.append("🔴 USD supports Risk OFF.")
elif USD_pct>-0.5 and USD_pct <=0.5:
    score+=0*3
    reasons.append("⚪ USD is stable.")
elif USD_pct>-1.5 and  USD_pct <=-0.5:
    score+=2*3
    reasons.append("🟢 Weaker USD supports Risk ON.")
elif USD_pct <=-1.5:
    score+=3*3
    reasons.append("🟢 Investors are moving away from defensive Dollar positions.")


if JPY_pct >1.5:
    score+=-3*3
    reasons.append("🔴 Investors are buying the Japanese Yen for safety.")
elif JPY_pct>0.5 and JPY_pct <=1.5:
    score+=-2*3
    reasons.append("🔴 Yen supports Risk OFF.")
elif JPY_pct>-0.5 and JPY_pct <=0.5:
    score+=0*3
    reasons.append("⚪ Yen is stable.")
elif JPY_pct>-1.5 and  JPY_pct <=-0.5:
    score+=2*3
    reasons.append("🟢 Yen weakness supports Risk ON.")
elif JPY_pct <=-1.5:
    score+=3*3
    reasons.append("🟢 Investors are rotating into risk assets.")


print(f"Score:{score}")
for reason in reasons:
    print(f"Reasons: {reason}")