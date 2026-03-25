import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np


def train_sarima(train_series, order=(1,1,1), seasonal_order=(1,1,1,7)):
    model = SARIMAX(train_series, order=order, seasonal_order=seasonal_order)
    fitted = model.fit(disp=False)
    return fitted


def forecast_sarima(model, steps):
    forecast = model.forecast(steps=steps)
    return forecast


def evaluate_forecast(true, pred):
    mape = mean_absolute_percentage_error(true, pred)
    rmse = np.sqrt(mean_squared_error(true, pred))
    return {"MAPE": mape, "RMSE": rmse}