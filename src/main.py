import logging
import os
import pandas as pd

from src.data_prep import load_and_merge, split_store_data
from src.eda import (
    plot_seasonality,
    promo_uplift,
    competition_scatter,
    store_type_performance
)
from src.modeling_sarima import train_sarima, forecast_sarima, evaluate_forecast
from src.modeling_prophet import (
    prepare_prophet_data,
    train_prophet,
    forecast_prophet,
    evaluate_prophet
)

# ---------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started.")

# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------
RAW_TRAIN = "data/raw/train.csv"
RAW_STORE = "data/raw/store.csv"
PROCESSED_DIR = "data/processed"
FIG_DIR = "reports/figures"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. Load & Merge
# ---------------------------------------------------------
logging.info("Loading and merging raw data...")
df = load_and_merge(RAW_TRAIN, RAW_STORE)
df.to_csv(f"{PROCESSED_DIR}/cleaned_merged.csv", index=False)
logging.info("Saved cleaned merged dataset.")

# ---------------------------------------------------------
# 2. EDA
# ---------------------------------------------------------
logging.info("Running EDA...")

plot_seasonality(df)
promo_uplift(df)
competition_scatter(df)
store_type_performance(df)

logging.info("EDA completed.")

# ---------------------------------------------------------
# 3. Forecasting (Store 1)
# ---------------------------------------------------------
logging.info("Preparing forecasting data...")

train, test = split_store_data(df, store_id=1)

# SARIMA
logging.info("Training SARIMA...")
sarima_model = train_sarima(train["Sales"])
sarima_forecast = forecast_sarima(sarima_model, steps=len(test))
sarima_metrics = evaluate_forecast(test["Sales"], sarima_forecast)
logging.info(f"SARIMA Metrics: {sarima_metrics}")

# Prophet
logging.info("Training Prophet...")
prophet_train = prepare_prophet_data(train)
prophet_model = train_prophet(prophet_train)
prophet_forecast = forecast_prophet(prophet_model, periods=len(test))
prophet_metrics = evaluate_prophet(test, prophet_forecast)
logging.info(f"Prophet Metrics: {prophet_metrics}")

logging.info("Pipeline completed successfully.")