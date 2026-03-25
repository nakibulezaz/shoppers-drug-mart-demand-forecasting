import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np


def prepare_prophet_data(train_df):
    df = train_df[["Date", "Sales"]].rename(columns={"Date": "ds", "Sales": "y"})
    return df


def train_prophet(train_df):
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    model.fit(train_df)
    return model


def forecast_prophet(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


def evaluate_prophet(test_df, forecast_df):
    test_df["Date"] = pd.to_datetime(test_df["Date"]).dt.tz_localize(None)
    forecast_df["ds"] = pd.to_datetime(forecast_df["ds"]).dt.tz_localize(None)

    merged = test_df.merge(
        forecast_df[["ds", "yhat"]],
        left_on="Date",
        right_on="ds",
        how="left"
    )

    mape = mean_absolute_percentage_error(merged["Sales"], merged["yhat"])
    rmse = np.sqrt(mean_squared_error(merged["Sales"], merged["yhat"]))

    return {"MAPE": mape, "RMSE": rmse}