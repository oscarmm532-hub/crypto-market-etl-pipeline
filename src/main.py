from extract import extract_market_data
from load import load_to_mongodb
from transform import transform_market_data


def run_pipeline():
  print("1. Extrayendo datos desde CoinGecko API...")
  raw_data = extract_market_data()

  print("2. Transformando y limpiando datos con Pandas...")
  clean_df = transform_market_data(raw_data)
  print(f"   Registros procesados: {len(clean_df)}")

  print("3. Guardando resultados...")
  load_to_mongodb(clean_df)
  print("Pipeline ETL finalizado con éxito.")


if __name__ == "__main__":
  run_pipeline()
