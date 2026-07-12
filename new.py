import yfinance as yf

def market():
    def fetch_nifty50():
        global nifty_pct
        try:
            t = yf.Ticker("^NSEI")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            nifty_pct = (price - prev) / prev * 100
            return {"price": price, "pct": nifty_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    def fetch_nasdaq():
        global nasdaq_pct
        try:
            t = yf.Ticker("^IXIC")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            nasdaq_pct = (price - prev) / prev * 100
            return {"price": price, "pct": nasdaq_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    def fetch_sp500():
        global sp500_pct
        try:
            t = yf.Ticker("^GSPC")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            sp500_pct = (price - prev) / prev * 100
            return {"price": price, "pct": sp500_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    def fetch_dowjones():
        global dowj_pct
        try:
            t = yf.Ticker("^DJI")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            dowj_pct = (price - prev) / prev * 100
            return {"price": price, "pct": dowj_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    def fetch_banknifty():
        global banknifty_pct
        try:
            t = yf.Ticker("^NSEBANK")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            banknifty_pct = (price - prev) / prev * 100
            return {"price": price, "pct": banknifty_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    def fetch_sensex():
        global sensex_pct
        try:
            t = yf.Ticker("^BSESN")
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            sensex_pct = (price - prev) / prev * 100
            return {"price": price, "pct": sensex_pct, "error": None}
        except Exception as e:
            return {"price": None, "pct": None, "error": str(e)}


    if __name__ == "__main__":
        print("📊 3. Global MARKETS")
        print("--------------------------")
        print("Index\t   Value     Change")
        print("--------------------------")

        nifty = fetch_nifty50()
        nasdaq = fetch_nasdaq()
        sp500 = fetch_sp500()
        dow = fetch_dowjones()
        banknifty = fetch_banknifty()
        sensex = fetch_sensex()

        for name, d in [
            ("NIFTY50", nifty),
            ("NASDAQ", nasdaq),
            ("S&P500", sp500),
            ("DOWJONES", dow),
            ("BANKNIFTY", banknifty),
            ("SENSEX", sensex),
        ]:
            if d["error"]:
                print(f"{name:<10} error: {d['error']}")
            else:
                print(f"{name:<10} {d['price']:.2f}  {d['pct']:+.2f}%")

market()