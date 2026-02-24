import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def build_daily_feature_matrix(orders_df, traffic_df):
    """
    Build multivariate daily feature matrix for anomaly detection.
    """

    # ---- Daily Revenue ----
    daily_revenue = (
        orders_df.groupby("order_date")["order_value"]
        .sum()
        .reset_index()
        .rename(columns={"order_date": "date"})
    )

    # ---- Daily Sessions ----
    daily_sessions = (
        traffic_df.groupby("date")["sessions"]
        .sum()
        .reset_index()
    )

    # ---- Merge ----
    df = pd.merge(daily_revenue, daily_sessions, on="date")

    # ---- Conversion Rate ----
    df["conversion_rate"] = df["order_value"] / df["sessions"]

    # ---- Revenue Concentration (Top Channel Share) ----
    channel_daily = (
        orders_df.groupby(["order_date", "channel"])["order_value"]
        .sum()
        .reset_index()
    )

    channel_daily["date"] = channel_daily["order_date"]

    pivot = (
        channel_daily.pivot(index="date", columns="channel", values="order_value")
        .fillna(0)
    )

    pivot["top_channel_share"] = pivot.max(axis=1) / pivot.sum(axis=1)

    pivot = pivot[["top_channel_share"]].reset_index()

    df = pd.merge(df, pivot, on="date")

    return df


def detect_ml_anomalies(feature_df, contamination=0.02, random_state=42):
    """
    Apply Isolation Forest for multivariate anomaly detection.
    """

    df = feature_df.copy()

    features = df[[
        "order_value",
        "sessions",
        "conversion_rate",
        "top_channel_share"
    ]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state
    )

    df["ml_anomaly_flag"] = model.fit_predict(X_scaled)
    df["ml_anomaly_flag"] = df["ml_anomaly_flag"].map({1: False, -1: True})

    return df