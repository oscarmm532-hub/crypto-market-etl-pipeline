# Cryptocurrency Market ETL Pipeline

An end-to-end automated ETL (Extract, Transform, Load) data pipeline built with Python, Pandas, and MongoDB to ingest, clean, and store real-time cryptocurrency market metrics.

## Architecture
`CoinGecko REST API` ➔ `Python (Requests & Pandas)` ➔ `MongoDB Atlas / CSV Backup`

## Project Structure
* `src/extract.py` — Fetches top 20 market assets from the CoinGecko API.
* `src/transform.py` — Cleans data types, handles nulls, and computes intraday volatility.
* `src/load.py` — Persists processed records into MongoDB Atlas (with CSV fallback).
* `src/main.py` — Orchestrates the end-to-end ETL workflow.
* `requirements.txt` — Project dependencies.

## Key Transformations & Feature Engineering
* **Schema & Type Enforcement:** Casts pricing, volume, and market cap fields to numeric types with safe null handling.
* **Text Standardization:** Normalizes ticker symbols to uppercase.
* **Intraday Volatility (`intraday_volatility_pct`):** Calculates the percentage spread between the 24-hour high and low prices.
* **UTC Audit Timestamp (`extracted_at`):** Tags every batch with an ISO-8601 UTC execution timestamp for historical tracking.

## How to Run Locally
1. Clone the repository and install dependencies:
```bash
git clone [https://github.com/oscarmm532-hub/crypto-market-etl-pipeline.git](https://github.com/oscarmm532-hub/crypto-market-etl-pipeline.git)
cd crypto-market-etl-pipeline
pip install -r requirements.txt

(Optional) Create a .env file in the root directory with your MongoDB connection string:
MONGO_URI=your_mongodb_atlas_connection_string
Run the pipeline:
python src/main.py
