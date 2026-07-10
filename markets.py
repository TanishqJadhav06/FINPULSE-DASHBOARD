from config import indices
import yfinance as yf


def market():
    print("📊 3. Global MARKETS")
    print("--------------------------")
    print("Index\t   Value     Change")
    print("--------------------------")
    for name, symbol in indices.items():
        try:
            t = yf.Ticker(symbol)
            price = t.fast_info["lastPrice"]
            prev = t.fast_info["previousClose"]
            pct = (price - prev) / prev * 100
            print(f"{name:<10} {price:.2f}  {pct:+.2f}%")
        except Exception as e:
            print(f"{name:<10} error: {e}")


market()