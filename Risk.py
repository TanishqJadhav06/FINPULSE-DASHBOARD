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
        score+=3*4*-1
        reasons.append("🔴 Gold is surging — strong safe-haven demand as fear grips markets")
    elif gold_pct >0.5 and gold_pct <=1.5:
        score+=2*4*-1
        reasons.append("🔴 Gold is climbing — investors turning cautious")
    elif gold_pct >-0.5 and gold_pct <=0.5:
        score+=0*4
        reasons.append("⚪ Gold is flat — no clear safe-haven signal today")
    elif gold_pct >-1.5 and gold_pct <=-0.5:
        score+=-2*4*-1
        reasons.append("🟢 Gold is easing — investors growing more confident")
    elif gold_pct<-1.5:
        score+=-3*4*-1
        reasons.append("🟢 Gold is falling sharply — strong risk appetite, fear has faded")
    else:
        print("Error getting value form gold")

#========================================silver====================================================================================#

    if silver_pct>1.5:
        score+=3*1*1
        reasons.append("🔴 Silver is spiking — safe-haven demand spilling into silver too")
    elif silver_pct >0.5 and silver_pct <=1.5:
        score+=2*1*-1
        reasons.append("🔴 Silver is up — modest defensive buying")
    elif silver_pct >-0.5 and silver_pct <=0.5:
        score+=0*1*-1
        reasons.append("⚪ Silver is flat — no strong signal")
    elif silver_pct >-1.5 and silver_pct <=-0.5:
        score+=-2*1*-1
        reasons.append("🟢 Silver is slipping — risk appetite improving")
    elif silver_pct<-1.5:
        score+=-3*1*-1
        reasons.append("🟢 Silver is falling sharply — confidence firmly back in risk assets")
    else:
        print("Error getting value form silver")

#========================================OIL====================================================================================#
    
    if oil_pct>1.5:
        score+=3*3*-1
        reasons.append("🔴 Rising oil prices increases inflation concerns.")
    elif oil_pct >0.5 and oil_pct <=1.5:
        score+=2*3*-1
        reasons.append("🔴 Oil is climbing — mild inflation and cost-push pressure building")
    elif oil_pct >-0.5 and oil_pct <=0.5:
        score+=0*3*-1
        reasons.append("⚪ Oil is stable — no inflation signal from energy today")
    elif oil_pct >-1.5 and oil_pct <=-0.5:
        score+=-2*3*-1
        reasons.append("🟢 Oil is easing — inflation pressure cooling off")
    elif oil_pct<-1.5:
        score+=-3*3*-1
        reasons.append("🟢 Oil is falling sharply — inflation risk easing, positive for rate outlook")
    else:
        print("Error getting value form oil")
    
#========================================naturalgas====================================================================================#
    '''
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
    '''
#========================================USD====================================================================================#

    if USD_pct >1.5:
        score+=3*3*-1
        reasons.append("🔴 Stronger USD reflects global demand for safety.")
    elif USD_pct>0.5 and USD_pct <=1.5:
        score+=2*3*-1
        reasons.append("🔴 Dollar is strengthening — pressure building on risk assets")
    elif USD_pct>-0.5 and USD_pct <=0.5:
        score+=0*3*-1
        reasons.append("⚪ Dollar is steady — no major currency signal today")
    elif USD_pct>-1.5 and  USD_pct <=-0.5:
        score+=-2*3*-1
        reasons.append("🟢 Dollar is weakening — easier global liquidity")
    elif USD_pct <=-1.5:
        score+=-3*3*-1
        reasons.append("🟢 Dollar is falling sharply — strong risk-on tailwind from a weaker dollar")
#========================================YEN====================================================================================#

    if JPY_pct >1.5:
        score+=3*2*-1
        reasons.append("🔴 Investors are buying the Japanese Yen for safety.")
    elif JPY_pct>0.5 and JPY_pct <=1.5:
        score+=2*2*-1
        reasons.append("🔴 Yen supports Risk OFF.")
    elif JPY_pct>-0.5 and JPY_pct <=0.5:
        score+=0*2*-1
        reasons.append("⚪ Yen is stable.")
    elif JPY_pct>-1.5 and JPY_pct <=-0.5:
        score+=-2*2*-1
        reasons.append("🟢 Yen weakness supports Risk ON.")
    elif JPY_pct <=-1.5:
        score+=-3*2*-1
        reasons.append("🟢 Investors are rotating into risk assets.")

#========================================EURO====================================================================================#
    '''
    if EUR_pct >1.5:
        score+=-3*1
        reasons.append("🔴 Euro reflects cautious investor positioning.")
    elif EUR_pct>-0.5 and EUR_pct <=0.5:
        score+=0*1
        reasons.append("⚪ Euro is neutral")
    elif EUR_pct <=-1.5:
        score+=3*1
        reasons.append("🟢 Euro supports improving market sentiment.")
    '''
#========================================CNY====================================================================================#
#========================================markets====================================================================================#
    if markets.nifty_pct >1.5:
        score+=3*4*1
        reasons.append("🟢 NIFTY is surging — strong bullish momentum in Indian equities")
    elif markets.nifty_pct>0.5 and markets.nifty_pct<=1.5:
        score+=2*4*1
        reasons.append("🟢 NIFTY is climbing — positive momentum building")
    elif markets.nifty_pct>-0.5 and markets.nifty_pct<=0.5:
        score+=0*4*1
        reasons.append("⚪ NIFTY is flat — no clear direction in Indian markets")
    elif markets.nifty_pct >=-1.5 and markets.nifty_pct <-0.5:
        score+=-2*4*1
        reasons.append("🔴 NIFTY is slipping — selling pressure building")
    elif markets.nifty_pct<-1.5:
        score+=-3*4*1
        reasons.append("🔴 NIFTY is falling sharply — strong bearish pressure on Indian equities")

#========================================markets====================================================================================#

    if markets.nasdaq_pct >1.5:
        score+=3*2*1
        reasons.append("🟢 Technology stocks are leading market gains.")
    elif markets.nasdaq_pct>0.5 and markets.nasdaq_pct<=1.5:
        score+=2*2*1
        reasons.append("🟢 Tech sector supports market optimism.")
    elif markets.nasdaq_pct>-0.5 and markets.nasdaq_pct<=0.5:
        score+=0*2*1
        reasons.append("⚪ Technology sector is stable.")
    elif markets.nasdaq_pct >=-1.5 and markets.nasdaq_pct <-0.5:
        score+=-2*2*1
        reasons.append("🔴 Technology stocks show increasing caution.")
    elif markets.nasdaq_pct<-1.5:
        score+=-3*2*1
        reasons.append("🔴 Heavy selling in technology.")


#========================================markets====================================================================================#


    if markets.sp500_pct >1.5:
        score+=3*4*1
        reasons.append("🟢 S&P 500 is surging — broad-based rally across US equities")
    elif markets.sp500_pct>0.5 and markets.sp500_pct<=1.5:
        score+=2*4*1
        reasons.append("🟢 S&P 500 is climbing — steady gains across the board")
    elif markets.sp500_pct>-0.5 and markets.sp500_pct<=0.5:
        score+=0*4*1
        reasons.append("⚪ S&P 500 is flat — US markets directionless today")
    elif markets.sp500_pct>=-1.5 and markets.sp500_pct<-0.5:
        score+=-2*4*1
        reasons.append("🔴 S&P 500 is slipping — broad market softness")
    elif markets.sp500_pct<-1.5:
        score+=-3*4*1
        reasons.append("🔴 S&P 500 is falling sharply — broad-based sell-off in US equities")


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
    '''
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
    '''
#========================================markets====================================================================================#
   
#========================================markets====================================================================================#    
    MarketMood=[]

    if score>=+50:
        MarketMood.append("🟢 Strong Risk ON")
    elif score<=20 and score<=+50:
        MarketMood.append("🟢 Risk ON")
    elif score>-20 and score<20:
        MarketMood.append("⚪ Neutral")
    elif score>-50 and score<-20 :
        MarketMood.append("🔴 Risk OFF")
    elif score<=-50:
        MarketMood.append("🔴 Strong Risk OFF")

    confidence=round((abs(score)/69)*100,1)

    from rich.table import Table
    from rich.console import Console
    from rich.box import Box
    from rich.panel import Panel
    consle=Console()
    table=Table()
    box=Box()

    print("===============================================================")
    print("📊 TODAY'S MARKET SIGNAL")
    print("===============================================================")
    
    print("Reasons\n------------------------")
    for market in MarketMood:
        print(f"Market Mood : {market}")
    print(f"Raw Score : {score} / 69")
    print(f"Confidence : {confidence:.2f}\n")

    for reason in reasons:
        print(f"{reason}")

if __name__=="__main__":
    risk()