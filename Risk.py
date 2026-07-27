

from rich.console import Console
from rich.table import Table
from rich import box

import percentage
import markets
import values
def risk():
    score=0

    reasons=[]

#========================================GOLD====================================================================================#
    if values.gold_pct>1.5:
        score+=3*4*-1
        reasons.append("🔴 Gold is surging — strong safe-haven demand as fear grips markets")
    elif values.gold_pct >0.5 and values.gold_pct <=1.5:
        score+=2*4*-1
        reasons.append("🔴 Gold is climbing — investors turning cautious")
    elif values.gold_pct >-0.5 and values.gold_pct <=0.5:
        score+=0*4
        reasons.append("⚪ Gold is flat — no clear safe-haven signal today")
    elif values.gold_pct >-1.5 and values.gold_pct <=-0.5:
        score+=-2*4*-1
        reasons.append("🟢 Gold is easing — investors growing more confident")
    elif values.gold_pct<-1.5:
        score+=-3*4*-1
        reasons.append("🟢 Gold is falling sharply — strong risk appetite, fear has faded")
    else:
        print("Error getting value form gold")

#========================================silver====================================================================================#

    if values.silver_pct>1.5:
        score+=3*1*1
        reasons.append("🔴 Silver is spiking — safe-haven demand spilling into silver too")
    elif values.silver_pct >0.5 and values.silver_pct <=1.5:
        score+=2*1*-1
        reasons.append("🔴 Silver is up — modest defensive buying")
    elif values.silver_pct >-0.5 and values.silver_pct <=0.5:
        score+=0*1*-1
        reasons.append("⚪ Silver is flat — no strong signal")
    elif values.silver_pct >-1.5 and values.silver_pct <=-0.5:
        score+=-2*1*-1
        reasons.append("🟢 Silver is slipping — risk appetite improving")
    elif values.silver_pct<-1.5:
        score+=-3*1*-1
        reasons.append("🟢 Silver is falling sharply — confidence firmly back in risk assets")
    else:
        print("Error getting value form silver")

#========================================OIL====================================================================================#
    
    if values.oil_pct>1.5:
        score+=3*3*-1
        reasons.append("🔴 Rising oil prices increases inflation concerns.")
    elif values.oil_pct >0.5 and values.oil_pct <=1.5:
        score+=2*3*-1
        reasons.append("🔴 Oil is climbing — mild inflation and cost-push pressure building")
    elif values.oil_pct >-0.5 and values.oil_pct <=0.5:
        score+=0*3*-1
        reasons.append("⚪ Oil is stable — no inflation signal from energy today")
    elif values.oil_pct >-1.5 and values.oil_pct <-0.5:
        score+=-2*3*-1
        reasons.append("🟢 Oil is easing — inflation pressure cooling off")
    elif values.oil_pct<-1.5:
        score+=-3*3*-1
        reasons.append("🟢 Oil is falling sharply — inflation risk easing, positive for rate outlook")
    else:
        print("Error getting value form oil")
    
#========================================naturalgas====================================================================================#

    if values.naturalgas_pct>1.5:
            score+=-1*3
            reasons.append("🔴 Natural gas prices suggest rising energy costs.")
    elif values.naturalgas_pct >0.5 and values.naturalgas_pct <=1.5:
            score+=-1*3
            reasons.append("🔴 Gas prices remain inflationary.")
    elif values.naturalgas_pct >-0.5 and values.naturalgas_pct <=0.5:
            score+=0*3
            reasons.append("⚪ Natural gas is stable.")
    elif values.naturalgas_pct >-1.5 and values.naturalgas_pct <=-0.5:
            score+=1*3
            reasons.append("🟢 Lower gas prices reduce energy cost pressure.")
    elif values.naturalgas_pct<=-1.5:
            score+=1*3
            reasons.append("🟢 Falling gas supports improving inflation expectations.")
    else:
        print("Error getting value form Natural Gas")

#========================================USD====================================================================================#

    if percentage.USD_pct >1.5:
        score+=3*3*-1
        reasons.append("🔴 Stronger USD reflects global demand for safety.")
    elif percentage.USD_pct>0.5 and percentage.USD_pct <=1.5:
        score+=2*3*-1
        reasons.append("🔴 Dollar is strengthening — pressure building on risk assets")
    elif percentage.USD_pct>-0.5 and percentage.USD_pct <=0.5:
        score+=0*3*-1
        reasons.append("⚪ Dollar is steady — no major currency signal today")
    elif percentage.USD_pct>-1.5 and  percentage.USD_pct <-0.5:
        score+=-2*3*-1
        reasons.append("🟢 Dollar is weakening — easier global liquidity")
    elif percentage.USD_pct <=-1.5:
        score+=-3*3*-1
        reasons.append("🟢 Dollar is falling sharply — strong risk-on tailwind from a weaker dollar")
#========================================YEN====================================================================================#

    if percentage.JPY_pct >1.5:
        score+=3*2*-1
        reasons.append("🔴 Investors are buying the Japanese Yen for safety.")
    elif percentage.JPY_pct>0.5 and percentage.JPY_pct <=1.5:
        score+=2*2*-1
        reasons.append("🔴 Yen supports Risk OFF.")
    elif percentage.JPY_pct>-0.5 and percentage.JPY_pct <=0.5:
        score+=0*2*-1
        reasons.append("⚪ Yen is stable.")
    elif percentage.JPY_pct>-1.5 and percentage.JPY_pct <=-0.5:
        score+=-2*2*-1
        reasons.append("🟢 Yen weakness supports Risk ON.")
    elif percentage.JPY_pct <=-1.5:
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
    table=Table(title="📊 TODAY'S MARKET SIGNAL",box=box.DOUBLE_EDGE,style=" white")
    console=Console()
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
    finaconfidence=str(f"{round(confidence):.1f}%")

    table.add_column("📝📈  Reasons",style="bold",justify="left")
    table.add_column("Overview")

    finalscore=str(f"{score}")
    for market in MarketMood:
        table.add_row("","Market Mood :"+market)
    table.add_row("","Raw Score :" +finalscore)
    table.add_row("","Confidence :" +finaconfidence+"\n")

    for reason in reasons[0:]:
        table.add_row(reason+"\n")

    console.print(table)
if __name__=="__main__":
    risk()