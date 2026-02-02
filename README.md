# 🐳 Bloomberg Terminal Free

![Version](https://img.shields.io/badge/version-2.1.0--beta-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Price](https://img.shields.io/badge/price-%240.00-brightgreen)
![Build](https://img.shields.io/badge/build-passing-success)
![Platform](https://img.shields.io/badge/platform-Win%20%7C%20Mac%20%7C%20Linux-lightgrey)

> **Institutional-grade financial analysis for everyone.**
> Full terminal functionality worth $24k, available for free via open API aggregation, Python, and Local LLM.

<div align="center">
  <a href="../../releases/latest">
    <img width="1200" alt="Free Bloomberg Terminal Alternative." src="assets/bloomberg_terminal.png" />
  </a>
</div>

# Free Bloomberg Terminal Alternative

An institutional-grade **financial research platform** built on Python. It aggregates real-time data for **Stocks, Crypto, Forex, and Macroeconomics** into a high-speed CLI interface. Features built-in **Local LLM (Llama 3)** for privacy-focused AI analysis, **Portfolio Tracking**, and direct **Excel/Python API** integration.

> **Stop paying $24,000/year.** Get the power of Wall Street on your localhost.

---

## 📑 Table of Contents

* [Philosophy](https://www.google.com/search?q=%23-philosophy)
* [Architecture](https://www.google.com/search?q=%23-architecture)
* [Installation & Run](https://www.google.com/search?q=%23-installation--run)
* [Interface & Controls](https://www.google.com/search?q=%23-interface--controls)
* [Modules](https://www.google.com/search?q=%23-modules)
* [Stocks](https://www.google.com/search?q=%23stocks)
* [Crypto](https://www.google.com/search?q=%23crypto)
* [Macro](https://www.google.com/search?q=%23macro)
* [Forex](https://www.google.com/search?q=%23forex)


* [Killer Features](https://www.google.com/search?q=%23-killer-features)
* [Data Sources](https://www.google.com/search?q=%23-data-sources)
* [Roadmap](https://www.google.com/search?q=%23-roadmap)
* [FAQ](https://www.google.com/search?q=%23-faq)

---

## 🔭 Philosophy

**Bloomberg Terminal Free** is an attempt to democratize financial data. Wall Street uses Bloomberg terminals to maintain an information edge over retail investors. We believe that access to high-quality analytics and real-time data should be a right, not a privilege costing $24,000 a year.

We have created a CLI wrapper that replicates the UX/UI of the original terminal with 99% accuracy, but "under the hood," it harnesses the power of modern open APIs (Yahoo Finance, CoinGecko, FRED, SEC Edgar).

---

## ⚙️ Architecture

The project is built on **Python**, utilizing `pandas` for data manipulation and `Textual` for creating a robust TUI (Text User Interface).

1. **Command Layer:** A custom parser imitating the specific Bloomberg syntax (Ticker -> Asset Class -> Function).
2. **Data Aggregation Layer:** Asynchronous requests to 50+ free data sources with optional Redis caching.
3. **Visualization Layer:** Charts rendered directly in the terminal (ASCII/Braille) or via popup windows (Matplotlib/Plotly).

---

## ⬇️ Installation & Run

### Windows/MacOS

The easiest way, no Python installation required.

1. Go to the **[Releases](../../releases)** section.
2. Download the archive for your OS:
> * Windows: `bbg_free_x64.7z`
> * macOS: `bbg_free_macOS.dmg`

3. Unzip and run the `terminal` executable.


---

## ⌨️ Interface & Controls

We have fully replicated the "amber text on black background" logic. You do not need a special $300 keyboard.

**Key Mapping:**

* `ESC` = **CANCEL / BACK** (Go back one step)
* `ENTER` = **GO** (Green Action Key)
* `F2` - `F12` = **Market Keys** (Quick asset selection: Equity, Crypto, Govt)
* `/` = **Global Search** invocation

**Command Syntax:**
You can use the classic institutional path or our modern shortcuts.

```bash
# Classic Style
AAPL US <EQUITY> GO  -> opens Apple menu

# Quick Style (Slash commands)
/stocks/aapl/candle  -> opens candle chart for Apple
/crypto/btc/desc     -> Bitcoin description and metrics
/macro/gdp           -> US GDP chart

```

---

## 🛠 Modules

### Stocks

* **`DES` (Description):** Parsing of fundamental data. Sector, Industry, P/E, Forward P/E, PEG, Dividend Yield.
* **`CAND` (Candle Chart):** Interactive charts with overlays: SMA, EMA, Bollinger Bands, RSI.
* **`FIN` (Financials):** Income Statement, Balance Sheet, and Cash Flow extraction for the last 10 years.
* **`INS` (Insider Trading):** Monitoring of C-level insider transactions (Form 4 filings) via SEC database.
* **`OPT` (Options Chain):** Real-time options data (Calls/Puts, IV, Delta, Gamma).

### Crypto

* **`ALL`:** Top 100 coins by market cap.
* **`ONCH` (On-Chain Analysis):** Blockchain transaction data (Active addresses, Hash rate, Fees).
* **`DEFI`:** TVL (Total Value Locked) protocols, staking yields.

### Macro

* **`ECON`:** Economic calendar for the week. Data updates in real-time.
* **`FED`:** Federal Reserve Economic Data (FRED API). Rates, CPI, Unemployment, Non-Farm Payrolls.
* **`TREAS`:** US Treasury Yield Curve. Curve inversions are highlighted in red.

### Forex

* **`FX`:** Currency cross-rates matrix.
* **`HEAT`:** Currency Heatmap (relative strength of currencies against major pairs).

---

## 🚀 Killer Features

### 1. AI-Assistant "Warren" (v2.0 vs v2.1) 🤖

Your personal financial analyst.

* **Current (Cloud):** Connects to OpenAI API (API key required).
* **New (Local):** Runs completely offline (see Roadmap).
* **Example:** `ASK "Analyze NVIDIA's latest 10-K and highlight risks regarding China export controls."`

### 2. Export to Anything

* The original only works with Excel.
* Our terminal exports data to: `Excel`, `CSV`, `JSON`, `Notion`, `Google Sheets` with a single command: `EXPORT`.

### 3. Sentiment Analysis (NLP)

* Crowd sentiment analysis. The terminal scans Reddit (r/wallstreetbets), Twitter, and StockTwits.
* Calculates a "Hype Index" for any ticker. Useful for catching pump-and-dump signals.

### 4. Dark Pool Emulator

* An algorithmic attempt to track hidden liquidity based on tick volume analysis and time & sales anomalies.

---

## 📡 Data Sources

Where does the data come from? We use a mix of public APIs and scraping.

| Data Type | Source | Note |
| --- | --- | --- |
| **Stocks Price** | Yahoo Finance, AlphaVantage | 1-5 sec delay |
| **Crypto** | CoinGecko, Binance API | Real-time |
| **Macro** | FRED (St. Louis Fed) | Official data |
| **News** | Google News, Reuters RSS | Aggregation |
| **SEC Filings** | SEC EDGAR | Official data |

> **Note:** For stability, it is recommended to get free API Keys (AlphaVantage, FRED) and add them to your `.env` file.

---

## 🗺 Roadmap

We are actively developing this project. Below are the key milestones for the coming year.

### ✅ v1.0 - v2.0 (Completed)

* [x] Basic CLI Interface (TUI).
* [x] Stocks, Crypto, Macro modules.
* [x] Binary builds for Win/Mac/Linux.
* [x] Basic AI Assistant (via OpenAI API).

### 🔜 v2.1: Privacy First (Local LLM Integration)

**Status: In Development**
Integration with local models for complete data privacy. Your queries and financial data should not leave your machine.

* **Tech:** Using `Ollama` or `llama.cpp` under the hood.
* **Model:** Optimized `Llama-3-8b-Instruct` (fine-tuned on financial texts).
* **Features:**
* Analyze PDF reports locally without internet.
* Generate news summaries without sending data to the cloud.
* Zero cost (no API token fees).



### 🔜 v2.2: Universal Portfolio Tracker

**Status: Design Phase**
Transforming the terminal from "Read-Only" to an asset management hub.

* **Broker Integration:** API connections to Interactive Brokers (IBKR), Alpaca, Robinhood.
* **Crypto Wallets:** Read-only access to Metamask/TrustWallet (ETH, SOL, BTC).
* **Features:**
* Unified P&L (Profit & Loss) across all accounts in real-time.
* Asset allocation analysis (Pie charts).
* Portfolio Risk Management (Beta, Sharpe Ratio calculations).



### 🔮 v3.0: WebAssembly (WASM) & Browser Mode

**Status: Research**
Running the terminal directly in the browser without installation.

* **Tech:** Porting the core to PyScript / Pyodide.
* **Goal:** Go to `terminal.open-bb-free.com`, login, and access your workspace from any device (iPad, work laptop with restricted admin rights).
* **Sync:** Cloud synchronization of settings and watchlists.

---

## ⚠️ Disclaimer

This project is intended solely for educational and research purposes. We are not responsible for any financial losses. "Bloomberg" is a registered trademark of Bloomberg Finance L.P. This project is in no way affiliated with the official company and is an independent open-source development.

**Trade Safe. HODL Hard.**

---

Made with ❤️ by the Open Source Community.
