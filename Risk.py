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
def risk():
    score=0

    reasons=[]
#========================================GOLD====================================================================================#
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

#========================================silver====================================================================================#

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

#========================================OIL====================================================================================#

    if oil_pct>1.5:
        score+=-2*3
        reasons.append("🔴 Rising oil prices increase inflation concerns.")
    elif oil_pct >0.5 and oil_pct <=1.5:
        score+=-1*3
        reasons.append("🔴 Oil is slightly inflationary.")
    elif oil_pct >-0.5 and oil_pct <0.5:
        score+=0*3
        reasons.append("⚪ Oil is stable today.")
    elif oil_pct >-1.5 and oil_pct <=-0.5:
        score+=1*3
        reasons.append("🟢 Lower oil eases inflation pressure.")
    elif oil_pct<-1.5:
        score+=2*3
        reasons.append("🟢 Falling oil supports Risk ON through lower inflation.")
    else:
        print("Error getting value form oil")

#========================================naturalgas====================================================================================#

    if naturalgas_pct>1.5:
        score+=-1*3
        reasons.append("🔴 Natural gas prices suggest rising energy costs.")
    elif naturalgas_pct >0.5 and naturalgas_pct <=1.5:
        score+=-1*3
        reasons.append("🔴 Gas prices remain inflationary.")
    elif naturalgas_pct >-0.5 and naturalgas_pct <0.5:
        score+=0*3
        reasons.append("⚪ Natural gas is stable.")
    elif naturalgas_pct >-1.5 and naturalgas_pct <=-0.5:
        score+=1*3
        reasons.append("🟢 Lower gas prices reduce energy cost pressure.")
    elif naturalgas_pct<=-1.5:
        score+=1*3
        reasons.append("🟢 Falling gas supports improving inflation expectations.")
    else:
        print("Error getting value form Natural Gas")

#========================================USD====================================================================================#

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
#========================================YEN====================================================================================#

    if JPY_pct >1.5:
        score+=-3*2
        reasons.append("🔴 Investors are buying the Japanese Yen for safety.")
    elif JPY_pct>0.5 and JPY_pct <=1.5:
        score+=-2*2
        reasons.append("🔴 Yen supports Risk OFF.")
    elif JPY_pct>-0.5 and JPY_pct <=0.5:
        score+=0*2
        reasons.append("⚪ Yen is stable.")
    elif JPY_pct>-1.5 and  JPY_pct <=-0.5:
        score+=2*2
        reasons.append("🟢 Yen weakness supports Risk ON.")
    elif JPY_pct <=-1.5:
        score+=3*2
        reasons.append("🟢 Investors are rotating into risk assets.")

#========================================EURO====================================================================================#

    if EUR_pct >1.5:
        score+=-3*1
        reasons.append("🔴 Euro reflects cautious investor positioning.")
    elif EUR_pct>-0.5 and EUR_pct <=0.5:
        score+=0*1
        reasons.append("⚪ Euro is neutral")
    elif EUR_pct <=-1.5:
        score+=3*1
        reasons.append("🟢 Euro supports improving market sentiment.")
#========================================CNY====================================================================================#

    if CNY_pct >1.5:
        score+=-3*1
        reasons.append("🔴 Stronger USD reflects global demand for safety.")
    elif CNY_pct>-0.5 and CNY_pct <=0.5:
        score+=0*0.5
        reasons.append("⚪ USD is stable.")
    elif CNY_pct <=-1.5:
        score+=3*1
        reasons.append("🟢 Investors are moving away from defensive Dollar positions.")

#========================================markets====================================================================================#
    if nifty_pct >1.5:
        score+=-3*4
        reasons.append("🟢 NIFTY is rallying strongly. Broad market sentiment is firmly Risk ON.")
    elif nifty_pct>0.5 and nifty_pct<=1.5:
        score+=-2*4
        reasons.append("🟢 NIFTY supports a positive market environment.")
    elif nifty_pct>-0.5 and nifty_pct<=0.5:
        score+=0*4
        reasons.append("⚪ NIFTY is trading sideways. No clear market direction.")
    elif nifty_pct >=-1.5 and nifty_pct <-0.5:
        score+=2*4
        reasons.append("🔴 NIFTY reflects increasing market caution.")
    elif nifty_pct<-1.5:
        score+=3*4
        reasons.append("🔴 NIFTY is selling off sharply. Strong Risk OFF sentiment.")

#========================================markets====================================================================================#

    if nasdaq_pct >1.5:
        score+=-3*2
        reasons.append("🟢 Technology stocks are leading market gains.")
    elif nasdaq_pct>0.5 and nasdaq_pct<=1.5:
        score+=-2*2
        reasons.append("🟢 Tech sector supports market optimism.")
    elif nasdaq_pct>-0.5 and nasdaq_pct<=0.5:
        score+=0*2
        reasons.append("⚪ Technology sector is stable.")
    elif nasdaq_pct >=-1.5 and nasdaq_pct <-0.5:
        score+=2*2
        reasons.append("🔴 Technology stocks show increasing caution.")
    elif nasdaq_pct<-1.5:
        score+=3*2
        reasons.append("🔴 Heavy selling in technology signals Risk OFF.")


#========================================markets====================================================================================#


    if sp500_pct >1.5:
        score+=-3*4
        reasons.append("🟢 S&P 500 reflects strong global Risk ON sentiment.")
    elif sp500_pct>0.5 and sp500_pct<=1.5:
        score+=-2*4
        reasons.append("🟢 Global equities remain supportive.")
    elif sp500_pct>-0.5 and sp500_pct<=0.5:
        score+=0*4
        reasons.append("⚪ S&P 500 is relatively unchanged.")
    elif sp500_pct>=-1.5 and sp500_pct<-0.5:
        score+=2*4
        reasons.append("🔴 Global investors are becoming more defensive.")
    elif sp500_pct<-1.5:
        score+=3*4
        reasons.append("🔴 Global markets are under heavy selling pressure.")


#========================================markets====================================================================================#


    if sensex_pct >1.5:
        score+=-3*3
        reasons.append("🟢 SENSEX confirms strong investor confidence.")
    elif sensex_pct>0.5 and sensex_pct<=1.5:
        score+=-2*3
        reasons.append("🟢 SENSEX supports a healthy equity market.")
    elif sensex_pct>-0.5 and sensex_pct<=0.5:
        score+=0*3
        reasons.append("⚪ SENSEX is stable today.")
    elif sensex_pct>=-1.5 and sensex_pct<-0.5:
        score+=2*3
        reasons.append("🔴 SENSEX reflects cautious investor sentiment.")
    elif sensex_pct<-1.5:
        score+=3*3
        reasons.append("🔴 SENSEX indicates broad market weakness.")

#========================================markets====================================================================================#
   
    if banknifty_pct >1.5:
        score+=-3*3
        reasons.append("🟢 Banking stocks are strengthening. Financial sector supports Risk ON.")
    elif banknifty_pct>0.5 and banknifty_pct<=1.5:
        score+=-2*3
        reasons.append("🟢 Banks are contributing positively to market momentum.")
    elif banknifty_pct>-0.5 and banknifty_pct<=0.5:
        score+=0*3
        reasons.append("⚪ Banking sector is stable.")
    elif banknifty_pct>=-1.5 and banknifty_pct<-0.5:
        score+=2*3
        reasons.append("🔴 Banking sector shows signs of caution.")
    elif banknifty_pct<-1.5:
        score+=3*3
        reasons.append("🔴 Banks are under heavy selling pressure. Risk appetite is weakening.")

#========================================markets====================================================================================#
   
    if dowj_pct>1.5:
        score+=-3*2
        reasons.append("🟢 Industrial stocks support economic confidence.")
    elif dowj_pct>0.5 and dowj_pct<=1.5:
        score+=-2*2
        reasons.append("🟢 Industrial sector remains positive.")
    elif dowj_pct>-0.5 and dowj_pct<=0.5:
        score+=0*2
        reasons.append("⚪ Industrial stocks are stable.")
    elif dowj_pct>=-1.5 and dowj_pct<-0.5:
        score+=2*2
        reasons.append("🔴 Industrial sector reflects growing caution.")
    elif dowj_pct<-1.5:
        score+=3*2
        reasons.append("🔴 Industrial weakness supports Risk OFF sentiment.")



#========================================markets====================================================================================#    
    MarketMood=[]

    if score<=-60:
        MarketMood.append("🟢 Strong Risk ON")
    elif score<=-25:
        MarketMood.append("🟢 Risk ON")
    elif score<25:
        MarketMood.append("⚪ Neutral")
    elif score<60:
        MarketMood.append("🔴 Risk OFF")
    else:
        MarketMood.append("🔴 Strong Risk OFF")

        
    confidence=round((abs(score)/93)*100,1)
    print("===============================================================")
    print("📊 FINPULSE MACRO SIGNAL (RISK)")
    print("===============================================================")
    
    print("Reasons\n------------------------")
    for market in MarketMood:
        print(f"Market Mood : {market}")
    print(f"Raw Score : {score} / 93")
    print(f"Confidence : {confidence:.2f}\n")

    for reason in reasons:
        print(f"{reason}")

risk()