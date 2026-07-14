import yfinance as yf

nifty_pct=0
nasdaq_pct=0
sp500_pct=0
dowj_pct=0
banknifty_pct=0
sensex_pct=0

def market():
    global nifty_pct
    global nasdaq_pct
    global sp500_pct
    global dowj_pct
    global banknifty_pct
    global sensex_pct
    

    print("📊 3. Global MARKETS")
    print("--------------------------")
    print("Index\t   Value     Change")
    print("--------------------------")
    for name, symbol in {"NIFTY50": "^NSEI"}.items():
        t = yf.Ticker(symbol)
        niftyprice = t.fast_info["lastPrice"]
        niftyprev = t.fast_info["previousClose"]
        nifty_pct=((niftyprice-niftyprev)/niftyprev)*100
        print(f"{name}    {niftyprice:.2f} {nifty_pct:+.2f}%")


    for name, symbol in {"NASDAQ": "^IXIC"}.items():
        t = yf.Ticker(symbol)
        nasprice = t.fast_info["lastPrice"]
        nasprev = t.fast_info["previousClose"]
        nasdaq_pct=((nasprice-nasprev)/nasprev)*100
        print(f"{name}     {nasprice:.2f} {nasdaq_pct:+.2f}%")


    for name, symbol in {"S&P500": "^GSPC"}.items():
        t = yf.Ticker(symbol)
        sp500price = t.fast_info["lastPrice"]
        sp500prev = t.fast_info["previousClose"]
        sp500_pct=((sp500price-sp500prev)/sp500prev)*100
        print(f"{name}     {sp500price:.2f}  {sp500_pct:+.2f}%")


    for name, symbol in {"DOWJONES": "^DJI"}.items():
        t = yf.Ticker(symbol)
        dowjprice = t.fast_info["lastPrice"]
        dowjprev = t.fast_info["previousClose"]
        dowj_pct=((dowjprice-dowjprev)/dowjprev)*100
        print(f"{name}   {dowjprice:.2f}  {dowj_pct:+.2f}%")

    for name, symbol in {"BANKNIFTY":"^NSEBANK"}.items():
        t = yf.Ticker(symbol)
        bankniftyprice = t.fast_info["lastPrice"]
        bankniftyprev = t.fast_info["previousClose"]
        banknifty_pct=((bankniftyprice-bankniftyprev)/bankniftyprev)*100
        print(f"{name}  {bankniftyprice:.2f}  {banknifty_pct:+.2f}%")

    for name, symbol in {"SENSEX":"^BSESN"}.items():
        t = yf.Ticker(symbol)
        sensexprice = t.fast_info["lastPrice"]
        sensexprev = t.fast_info["previousClose"]
        sensex_pct=((sensexprice-sensexprev)/sensexprev)*100
        print(f"{name}     {sensexprice:.2f}  {sensex_pct:+.2f}%")

if __name__=="__main__":
    market()