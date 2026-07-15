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

import markets
def risk():
    score=0

    reasons=[]
#========================================GOLD====================================================================================#
    if gold_pct>1.5:
        score+=-3*3
        reasons.append("🔴 Gold strongly supports Risk OFF. Strong flight to safety suggests elevated market fear.")
    elif gold_pct >0.5 and gold_pct <=1.5:
        score+=-2*3
        reasons.append("🔴 Gold supports Risk OFF. Investors are showing increased demand for safe-haven assets.")
    elif gold_pct >-0.5 and gold_pct <=0.5:
        score+=0*3
        reasons.append("⚪ Gold is neutral. No meaningful safe-haven signal today.")
    elif gold_pct >-1.5 and gold_pct <=-0.5:
        score+=2*3
        reasons.append("🟢 Gold supports Risk ON. Investors are gradually moving away from defensive assets")
    elif gold_pct<-1.5:
        score+=3*3 
        reasons.append("🟢 Gold strongly supports Risk ON. Safe-haven demand is falling, indicating strong investor confidence.")
    else:
        print("Error getting value form gold")

#========================================silver====================================================================================#

    if silver_pct>1.5:
        score+=-3*1
        reasons.append("🔴 Silver rises sharply, supporting a defensive market tone.")
    elif silver_pct >0.5 and silver_pct <=1.5:
        score+=-2*1
        reasons.append("🔴 Silver is up moderately, showing mild defensive positioning..")
    elif silver_pct >-0.5 and silver_pct <=0.5:
        score+=0*1
        reasons.append("⚪ Silver is neutral today.")
    elif silver_pct >-1.5 and silver_pct <=-0.5:
        score+=2*1
        reasons.append("🟢 Silver drops mildly, reflecting lower safe-haven demand.")
    elif silver_pct<-1.5:
        score+=3*1
        reasons.append("🟢 Silver drops sharply, supporting broader economic optimism.")
    else:
        print("Error getting value form silver")

#========================================OIL====================================================================================#

    if oil_pct>1.5:
        score+=-2*3
        reasons.append("🔴 Rising oil prices increase inflation concerns.")
    elif oil_pct >0.5 and oil_pct <=1.5:
        score+=-1*3
        reasons.append("🔴 Oil is slightly inflationary.")
    elif oil_pct >-0.5 and oil_pct <=0.5:
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
    elif naturalgas_pct >-0.5 and naturalgas_pct <=0.5:
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
#========================================markets====================================================================================#
    if markets.nifty_pct >1.5:
        score+=-3*4
        reasons.append("🟢 NIFTY is rallying strongly. Broad market sentiment is firmly Risk ON.")
    elif markets.nifty_pct>0.5 and markets.nifty_pct<=1.5:
        score+=-2*4
        reasons.append("🟢 NIFTY supports a positive market environment.")
    elif markets.nifty_pct>-0.5 and markets.nifty_pct<=0.5:
        score+=0*4
        reasons.append("⚪ NIFTY is trading sideways. No clear market direction.")
    elif markets.nifty_pct >=-1.5 and markets.nifty_pct <-0.5:
        score+=2*4
        reasons.append("🔴 NIFTY reflects increasing market caution.")
    elif markets.nifty_pct<-1.5:
        score+=3*4
        reasons.append("🔴 NIFTY is selling off sharply. Strong Risk OFF sentiment.")

#========================================markets====================================================================================#

    if markets.nasdaq_pct >1.5:
        score+=-3*2
        reasons.append("🟢 Technology stocks are leading market gains.")
    elif markets.nasdaq_pct>0.5 and markets.nasdaq_pct<=1.5:
        score+=-2*2
        reasons.append("🟢 Tech sector supports market optimism.")
    elif markets.nasdaq_pct>-0.5 and markets.nasdaq_pct<=0.5:
        score+=0*2
        reasons.append("⚪ Technology sector is stable.")
    elif markets.nasdaq_pct >=-1.5 and markets.nasdaq_pct <-0.5:
        score+=2*2
        reasons.append("🔴 Technology stocks show increasing caution.")
    elif markets.nasdaq_pct<-1.5:
        score+=3*2
        reasons.append("🔴 Heavy selling in technology signals Risk OFF.")


#========================================markets====================================================================================#


    if markets.sp500_pct >1.5:
        score+=-3*4
        reasons.append("🟢 S&P 500 reflects strong global Risk ON sentiment.")
    elif markets.sp500_pct>0.5 and markets.sp500_pct<=1.5:
        score+=-2*4
        reasons.append("🟢 Global equities remain supportive.")
    elif markets.sp500_pct>-0.5 and markets.sp500_pct<=0.5:
        score+=0*4
        reasons.append("⚪ S&P 500 is relatively unchanged.")
    elif markets.sp500_pct>=-1.5 and markets.sp500_pct<-0.5:
        score+=2*4
        reasons.append("🔴 Global investors are becoming more defensive.")
    elif markets.sp500_pct<-1.5:
        score+=3*4
        reasons.append("🔴 Global markets are under heavy selling pressure.")


#========================================markets====================================================================================#

    '''
        if markets.sensex_pct >1.5:
            score+=-3*3
            reasons.append("🟢 SENSEX confirms strong investor confidence.")
        elif markets.sensex_pct>0.5 and markets.sensex_pct<=1.5:
            score+=-2*3
            reasons.append("🟢 SENSEX supports a healthy equity market.")
        elif markets.sensex_pct>-0.5 and markets.sensex_pct<=0.5:
            score+=0*3
            reasons.append("⚪ SENSEX is stable today.")
        elif markets.sensex_pct>=-1.5 and markets.sensex_pct<-0.5:
            score+=2*3
            reasons.append("🔴 SENSEX reflects cautious investor sentiment.")
        elif markets.sensex_pct<-1.5:
            score+=3*3
            reasons.append("🔴 SENSEX indicates broad market weakness.")
    '''
#========================================markets====================================================================================#
   
    if markets.banknifty_pct >1.5:
        score+=-3*3
        reasons.append("🟢 Banking stocks are strengthening. Financial sector supports Risk ON.")
    elif markets.banknifty_pct>0.5 and markets.banknifty_pct<=1.5:
        score+=-2*3
        reasons.append("🟢 Banks are contributing positively to market momentum.")
    elif markets.banknifty_pct>-0.5 and markets.banknifty_pct<=0.5:
        score+=0*3
        reasons.append("⚪ Banking sector is stable.")
    elif markets.banknifty_pct>=-1.5 and  markets.banknifty_pct<-0.5:
        score+=2*3
        reasons.append("🔴 Banking sector shows signs of caution.")
    elif markets.banknifty_pct<-1.5:
        score+=3*3
        reasons.append("🔴 Banks are under heavy selling pressure. Risk appetite is weakening.")

#========================================markets====================================================================================#
   
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

if __name__=="__main__":
    risk()