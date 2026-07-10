# 📈 FINPULSE

**FINPULSE** is a Python-based financial dashboard that brings together live market information from multiple APIs into one clean command-line interface.

The project provides real-time data for commodities, currencies, global stock indices, and financial news while also calculating daily percentage changes using historical market data.

This project was built as my CS50P Final Project and continues to evolve with new features.

---

## Features

### 🏅 Commodities

- Gold
- Silver
- Crude Oil
- Natural Gas
- Corn
- Wheat

Displays:

- Current Price
- Daily Percentage Change (implemented for supported assets)

---

### 🌍 Global Currencies

Track major currency pairs such as:

- USD/INR
- EUR/INR
- GBP/INR
- JPY/INR

Displays:

- Live Exchange Rate
- Daily Percentage Change

---

### 📊 Global Markets

Live data for major indices including:

- NIFTY 50
- SENSEX
- BANKNIFTY
- NASDAQ
- S&P 500
- Dow Jones

---

### 📰 Financial News

Displays the latest market-related headlines from trusted news APIs.

---

### 📈 Percentage Change Engine

FINPULSE compares today's live market price with historical market data to calculate daily percentage changes.

---

## Project Structure

```
FINPULSE
│
├── main.py
├── commodities.py
├── currencies.py
├── markets.py
├── news.py
├── percentage.py
├── values.py
├── config.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies Used

- Python
- Requests
- JSON
- Datetime
- Multiple Financial APIs
- Yahoo Finance (yfinance)

---

## Future Features

- Rich Terminal UI
- SQLite Database
- Market Risk Engine
- Market Summary
- Telegram Bot
- Portfolio Tracking
- Charts and Data Visualization

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/FINPULSE.git
```

Move into the project folder

```bash
cd FINPULSE
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
API_KEY=YOUR_API_KEY
NEWS_API_KEY=YOUR_KEY
TWELVE_DATA_KEY=YOUR_KEY
```

Run the project

```bash
python main.py
```

---

## Example Output

```
===============================
        FINPULSE
===============================

🏅 Commodities

Gold ............ 4123.72 (+1.46%)
Silver .......... 60.14 (+3.90%)
Crude Oil ....... 76.61 (+0.03%)

🌍 Global Currencies

USD/INR ......... 85.52 (+0.12%)
EUR/INR ......... 100.08 (-0.22%)

📊 Global Markets

NIFTY50 ......... +0.52%
NASDAQ .......... -0.17%

📰 Top Headlines

• Headline 1
• Headline 2
• Headline 3
```

---

## Learning Outcomes

Building FINPULSE helped me learn:

- Working with REST APIs
- Parsing JSON data
- Modular Python architecture
- Error handling
- Historical market data
- Financial data processing
- Project organization
- Real-world software development

---

## Roadmap

- [x] Live Commodities
- [x] Commodity Percentage Changes
- [x] Live Currency Rates
- [x] Currency Percentage Changes
- [x] Global Markets
- [x] Financial News
- [ ] Risk Engine
- [ ] Market Summary
- [ ] SQLite Integration
- [ ] Rich Dashboard
- [ ] Telegram Bot

---

Made with ❤️ using Python.
