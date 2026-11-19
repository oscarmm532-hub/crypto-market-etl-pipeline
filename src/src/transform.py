from datetime import datetime, timezone
import pandas as pd


def transform_market_data(raw_data):
  df = pd.DataFrame(raw_data)

  # Seleccionar columnas relevantes
  cols = [
      "id",
      "symbol",
      "name",
      "current_price",
      "market_cap",
      "total_volume",
      "high_24h",
      "low_24h",
      "price_change_percentage_24h",
  ]
  df = df[cols].copy()

  # Asegurar tipos numéricos y manejar posibles valores nulos
  numeric_cols = [
      "current_price",
      "market_cap",
      "total_volume",
      "high_24h",
      "low_24h",
      "price_change_percentage_24h",
  ]
  for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

  # Normalizar texto
  df["symbol"] = df["symbol"].str.upper().str.strip()

  # Ingeniería de características: volatilidad porcentual en las últimas 24h
  df["intraday_volatility_pct"] = (
      (df["high_24h"] - df["low_24h"]) / df["low_24h"].replace(0, pd.NA)
  ) * 100
  df["intraday_volatility_pct"] = (
      df["intraday_volatility_pct"].fillna(0.0).round(2)
  )

  # Marca de tiempo de ejecución en UTC
  df["extracted_at"] = datetime.now(timezone.utc).isoformat()

  return df
