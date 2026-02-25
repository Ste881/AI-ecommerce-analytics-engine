import pandas as pd
import numpy as np
from prophet import Prophet


def build_daily_revenue_series(orders_df):
    """
    Aggregate orders into daily revenue time series.
    """
    df = (
        orders_df.groupby("order_date")["order_value"]
        .sum()
        .reset_index()
        .rename(columns={"order_date": "ds", "order_value": "y"})
    )

    df["ds"] = pd.to_datetime(df["ds"])

    return df


def train_prophet_model(revenue_df):
    """
    Train Prophet model on daily revenue.
    """
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(revenue_df)

    return model


def forecast_revenue(model, periods=30):
    """
    Forecast future revenue.
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast


def compute_residual_anomalies(revenue_df, forecast_df, z_threshold=2.5):
    """
    Detect anomalies using residual (actual - forecast).
    """

    merged = pd.merge(
        revenue_df,
        forecast_df[["ds", "yhat"]],
        on="ds"
    )

    merged["residual"] = merged["y"] - merged["yhat"]

    mean_res = merged["residual"].mean()
    std_res = merged["residual"].std()

    merged["residual_z"] = (
        (merged["residual"] - mean_res) / std_res
    )

    merged["forecast_anomaly"] = merged["residual_z"].abs() > z_threshold

    return merged