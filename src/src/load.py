import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def load_to_mongodb(df):
  uri = os.getenv("MONGO_URI")

  if not uri:
    print("MONGO_URI no encontrado. Guardando respaldo local en CSV...")
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/market_snapshot_backup.csv", index=False)
    return

  client = MongoClient(uri)
  db = client["crypto_etl_db"]
  collection = db["market_snapshots"]

  records = df.to_dict(orient="records")
  if records:
    collection.insert_many(records)
    print(f"Se insertaron {len(records)} registros en MongoDB Atlas.")
