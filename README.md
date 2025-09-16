# 📊 Jaehyeon Jeong's Data Portfolio

Welcome! I'm a 4th-year Computer Science & Applied Mathematics student This portfolio highlights practicing Python, SQL, Tableau, and more

---

## 🧠 About Me
- 🎓 4th-year CS & Applied Mathematics student at MIPT
- 📈 Interested in data analysis, visualization, cryptocurrency and real-world impact through data
- 💡 Currently learning: Predictive analytics, A/B testing, and dashboard design
- 🧑‍💻 Preparing for a Data Analyst 

---
# 📊 Crypto Data Analyst Portfolio

This repository showcases my preparation for **Data Analyst / Research Analyst roles** in **Crypto & DeFi** (e.g., Binance, Web3 analytics).  
It combines **ETL pipelines, SQL/GraphQL queries, on-chain dashboards, and tokenomics research**.

---

## 🗂️ Repository Map

### 1. Python & SQL Practice
- `python_practice/`: LeetCode solutions (easy → hard), Green Book quant interview problems.
- `sql_practice/`: SQL query problems from LeetCode.
- 
### 2. ETL Pipelines (`etl/`)
- Binance REST API → fetch historical & live trade/klines data.
- GraphQL queries (Uniswap Subgraph, others) → fetch pool metrics, liquidity, volume.
- Data stored in **Parquet/CSV** for analytics.
- Example: `etl_binance.py` → pulls BTCUSDT 1m klines for last 7 days → saves as Parquet.

### 3. SQL & Queries (`queries/`)
- SQL queries (DuckDB/ClickHouse) for aggregated analytics:
  - Average spreads by hour.
  - Daily trading volume.
  - Wallet activity summaries.
- GraphQL queries → pool fees, TVL, token swaps.

### 4. Dashboards (`dashboards/`)
- **Tableau Dashboards**:
  - OHLC + volume visualization from Binance API data.
  - User growth / wallet activity trends.
- **Dune Dashboards**:
  - DEX volume & liquidity.
  - Stablecoin flow analysis.
- Screenshots in `images/` + live links provided.

### 5. Tokenomics Reports (`reports/`)
- Research-style writeups analyzing:
  - Protocol tokenomics (supply emissions, FDV vs float).
  - Holder concentration (whales vs retail).
  - Liquidity mining incentives.
- Each report = Markdown/PDF with visuals.

### 6. Exploratory Notebooks (`notebooks/`)
- Jupyter notebooks for:
  - Cleaning + aggregating Binance data.
  - Feature extraction (volatility, volume spikes).
  - On-chain metric analysis.

---

## 📈 Weekly Progress

| Week | Python LeetCode | SQL LeetCode | ETL | Dashboards | Reports | Notes |
|------|-----------------|--------------|-----|------------|---------|-------|
| 1    | 10 problems     | 5 problems   | Binance API script | Tableau basics | - | Setup |
| 2    | 15 problems     | 10 problems  | GraphQL subgraph  | Dune dashboard | Tokenomics note | - |
| 3    | 20 problems     | 15 problems  | Automated ETL job | Tableau + Dune v2 | Full report draft | - |

---

## 🔗 Related Portfolio
- [Quant Researcher Repo](https://github.com/yourusername/quant-researcher) → Probability, Statistics Backtests, LOB features, ML models, Kaggle-style projects.
