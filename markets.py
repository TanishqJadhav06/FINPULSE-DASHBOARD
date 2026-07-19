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

    from rich.console import Console
    from rich.table import Table
    from rich import box
    console=Console()
    table=Table(title="📊 3. Global MARKETS",box=box.DOUBLE_EDGE,border_style="bright_blue")

    table.add_column("Index",style="bold cyan")
    table.add_column("Value",style="bold white",justify="right")
    table.add_column("Change",style="bold green",justify="right")

    for name, symbol in {"NIFTY50": "^NSEI"}.items():
        t = yf.Ticker(symbol)
        niftyprice = t.fast_info["lastPrice"]
        niftyprev = t.fast_info["previousClose"]
        nifty_pct=((niftyprice-niftyprev)/niftyprev)*100
        nifty_pctn=(f"{nifty_pct:+.2f}%")
        niftyrate=str(f"{niftyprice:.2f}")
        table.add_row(name,niftyrate,nifty_pctn)

    for name, symbol in {"NASDAQ": "^IXIC"}.items():
        t = yf.Ticker(symbol)
        nasprice = t.fast_info["lastPrice"]
        nasprev = t.fast_info["previousClose"]
        nasdaq_pct=((nasprice-nasprev)/nasprev)*100
        nasdaq_pctn=(f"{nasdaq_pct:+.2f}%")
        nasdaqrate=str(f"{nasprice:.2f}")
        table.add_row(name,nasdaqrate,nasdaq_pctn)


    for name, symbol in {"S&P500": "^GSPC"}.items():
        t = yf.Ticker(symbol)
        sp500price = t.fast_info["lastPrice"]
        sp500prev = t.fast_info["previousClose"]
        sp500_pct=((sp500price-sp500prev)/sp500prev)*100
        sp500_pctn=(f"{sp500_pct:+.2f}%")
        sp500rate=str(f"{sp500price:.2f}")
        table.add_row(name,sp500rate,sp500_pctn)


    for name, symbol in {"DOWJONES": "^DJI"}.items():
        t = yf.Ticker(symbol)
        dowjprice = t.fast_info["lastPrice"]
        dowjprev = t.fast_info["previousClose"]
        dowj_pct=((dowjprice-dowjprev)/dowjprev)*100
        dowj_pctn=(f"{dowj_pct:+.2f}%")
        dowjrate=str(f"{dowjprice:.2f}")
        table.add_row(name,dowjrate,dowj_pctn)

    for name, symbol in {"BANKNIFTY":"^NSEBANK"}.items():
        t = yf.Ticker(symbol)
        bankniftyprice = t.fast_info["lastPrice"]
        bankniftyprev = t.fast_info["previousClose"]
        banknifty_pct=((bankniftyprice-bankniftyprev)/bankniftyprev)*100
        banknifty_pctn=(f"{banknifty_pct:+.2f}%")
        bankniftyrate=str(f"{bankniftyprice:.2f}")
        table.add_row(name,bankniftyrate,banknifty_pctn)

    for name, symbol in {"SENSEX":"^BSESN"}.items():
        t = yf.Ticker(symbol)
        sensexprice = t.fast_info["lastPrice"]
        sensexprev = t.fast_info["previousClose"]
        sensex_pct=((sensexprice-sensexprev)/sensexprev)*100
        sensex_pctn=(f"{sensex_pct:+.2f}%")
        sensexrate=str(f"{sensexprice:.2f}")
        table.add_row(name,sensexrate,sensex_pctn)

        
    console.print(table)
if __name__=="__main__":
    market()