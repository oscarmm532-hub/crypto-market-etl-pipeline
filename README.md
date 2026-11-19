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

Key Transformations & Feature Engineering 
* Schema & Type Enforcement: Casts pricing, volume, and market cap fields to numeric types with safe null handling.

* Text Standardization: Normalizes ticker symbols to uppercase.

* Intraday Volatility (intraday_volatility_pct): Calculates the percentage spread between the 24-hour high and low prices.

* UTC Audit Timestamp (extracted_at): Tags every batch with an ISO-8601 UTC execution timestamp for historical tracking.


git clone [https://github.com/oscarmm532-hub/crypto-market-etl-pipeline.git](https://github.com/oscarmm532-hub/crypto-market-etl-pipeline.git)
cd crypto-market-etl-pipeline
pip install -r requirements.txt
MONGO_URI=tu_cadena_de_conexion_de_mongodb_atlas
python src/main.py

