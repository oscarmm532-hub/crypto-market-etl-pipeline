# Cryptocurrency Market ETL Pipeline

An end-to-end automated ETL (Extract, Transform, Load) data pipeline built with Python, Pandas, and MongoDB to ingest, clean, and store real-time cryptocurrency market metrics.

## Architecture
`CoinGecko REST API` ➔ `Python (Requests & Pandas)` ➔ `MongoDB Atlas / CSV Backup`

## Project Structure
```text
├── src/
│   ├── extract.py      # Fetches top 20 market assets from CoinGecko API
│   ├── transform.py    # Cleans data types, handles nulls, and computes intraday volatility
│   ├── load.py         # Persists processed records into MongoDB Atlas (with CSV fallback)
│   └── main.py         # Orchestrates the end-to-end ETL workflow
├── requirements.txt    # Project dependencies
└── README.md
