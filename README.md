# 📈 FINPULSE v1.0

**Personal Macro Intelligence Terminal**

*Know the markets. Understand the big picture.*

FINPULSE is a terminal-based macro dashboard that pulls live commodities, currency, and global index data into a single glanceable screen — then runs it through a weighted scoring engine to tell you whether the market mood is **Risk ON** or **Risk OFF**, with a confidence score and plain-English reasoning behind every call.

Built entirely in Python with [Rich](https://github.com/Textualize/rich) for the terminal UI — no web server, no browser, just a live-refreshing console dashboard.

---

## What it does

| Panel | What's in it |
|---|---|
| 🛢️ **Commodities** | Gold, Silver, Crude Oil (WTI), Natural Gas, Corn, Wheat — price + 1-day % change |
| 🌐 **Global Currencies** | USD, EUR, JPY, GBP, CNY, AUD — all quoted against INR |
| 📊 **Global Markets** | NIFTY50, NASDAQ, S&P500, DOWJONES, BANKNIFTY, SENSEX |
| 🎯 **Market Signal** | A weighted Risk ON / Risk OFF call, with a confidence % and the reasoning behind it |
| 🗞️ **Top Headlines** | Latest business headlines, pulled live |

Everything renders as a set of bordered panels laid out in a responsive grid — resize your terminal and the layout stretches with it.

---

## How the Risk Signal works

FINPULSE scores nine macro signals — Gold, Silver, Crude Oil, Natural Gas, USD/INR, JPY, NIFTY50, NASDAQ, and S&P500 — each on a five-tier scale (strong move down → flat → strong move up), weighted by how much that asset typically matters to risk sentiment.

The signals are summed into a raw score, which maps to:

- 🟢 **Strong Risk ON** / **Risk ON**
- ⚪ **Neutral**
- 🔴 **Risk OFF** / **Strong Risk OFF**

A confidence percentage (`|score| ÷ max possible score × 100`) tells you how strong the signal is, and every contributing reason — e.g. *"Gold is climbing — investors turning cautious"* — is listed so the call is never a black box.

---

## Tech stack

- **Python 3.12**
- [`rich`](https://github.com/Textualize/rich) — all terminal rendering (tables, panels, grids, color)
- [`yfinance`](https://github.com/ranaroussi/yfinance) — live index data (NIFTY, NASDAQ, S&P500, etc.)
- [`requests`](https://docs.python-requests.org/) — REST calls to commodity/currency/news APIs
- [`python-dotenv`](https://github.com/theskumar/python-dotenv) — API keys loaded from a local `.env`, never hardcoded

**Data sources:**
- [CommodityPriceAPI](https://commoditypriceapi.com/) — Gold, Silver, Crude Oil
- [EODHD](https://eodhd.com/) — Natural Gas
- [Alpha Vantage](https://www.alphavantage.co/) — Corn, Wheat
- [Frankfurter](https://frankfurter.dev/) — Currency exchange rates (no key required)
- [NewsAPI](https://newsapi.org/) — Top business headlines
- `yfinance` — Global and Indian index prices

---

## Project structure

```
FINPULSE/
├── main.py            # Entry point — assembles the grid, prints the dashboard
├── header.py           # Date/time, title block, "last updated" panel
├── commodities.py       # Gold, Silver, Oil, Natural Gas, Corn, Wheat panel
├── currencies.py        # USD/EUR/JPY/GBP/CNY/AUD vs INR panel
├── markets.py           # Global & Indian index panel
├── Risk.py              # Weighted scoring engine — Risk ON/OFF + reasons
├── news.py              # Top market headlines panel
├── config.py             # All API calls and environment setup
├── values.py             # % change calculations for commodities
├── percentage.py          # % change calculations for currencies
└── .env                  # API keys (not committed)
```

Fetch logic and Rich rendering are kept separate throughout — each panel module returns a renderable `Table`/`Panel` object; `main.py` is the only file that decides layout and prints to the console.

---

## Setup

1. Clone the repo and install dependencies:

```bash
git clone https://github.com/TanishqJadhav06/FINPULSE-DASHBOARD.git
cd FINPULSE-DASHBOARD
pip install rich requests yfinance python-dotenv
```

2. Create a `.env` file in the project root with your API keys:

```
COMMODITY_API_KEY=your_key_here
ALPHAVANTAGE_API_KEY=your_key_here
NEWSAPI_KEY=your_key_here
API_TOKEN=your_eodhd_token_here
```

3. Run it:

```bash
python main.py
```

---

## Roadmap

- [ ] SQLite persistence (`data/market.db`) — store historical snapshots for trend tracking
- [ ] True 7-day sparkline trends per asset (currently price + 1-day change only)
- [ ] Auto-refresh loop instead of manual re-run
- [ ] `[R] Refresh` / `[H] History` / `[S] Save` keyboard shortcuts

---

## Author

Built by **[TanishqJadhav06](https://github.com/TanishqJadhav06)** — a personal project to combine a Python CLI habit with an interest in macro markets and fintech.

---

*FINPULSE v1.0 — released July 31, 2026.*
