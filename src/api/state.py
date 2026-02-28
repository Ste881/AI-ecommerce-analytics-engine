import pandas as pd

from src.analytics.kpis import compute_kpis
from src.analytics.anomaly_detection import detect_statistical_anomalies
from src.analytics.ml_anomaly_detection import (
    build_daily_feature_matrix,
    detect_ml_anomalies
)
from src.analytics.forecasting import (
    build_daily_revenue_series,
    train_prophet_model,
    forecast_revenue,
    compute_residual_anomalies
)
from src.analytics.insights_engine import generate_structured_insights


class AppState:
    def __init__(self):
        self.kpis = None
        self.insights = None
        self.stat_anomalies = None
        self.ml_anomalies = None
        self.forecast_anomalies = None
        self.forecast_full = None


def load_and_compute_state() -> AppState:
    """
    Load CSV data and precompute all analytics outputs.
    Runs once on API startup.
    """

    state = AppState()

    # -------------------------
    # Load data
    # -------------------------
    orders_df = pd.read_csv("data/orders.csv")
    traffic_df = pd.read_csv("data/website_traffic.csv")

    # -------------------------
    # KPIs
    # -------------------------
    kpis = compute_kpis(orders_df, traffic_df)
    state.kpis = kpis

    # -------------------------
    # Statistical anomalies
    # -------------------------
    daily_revenue = (
        orders_df.groupby("order_date")["order_value"]
        .sum()
        .reset_index()
        .rename(columns={"order_date": "date"})
    )

    stat_df = detect_statistical_anomalies(
        daily_revenue,
        value_column="order_value"
    )

    state.stat_anomalies = stat_df

    # -------------------------
    # ML anomalies
    # -------------------------
    feature_df = build_daily_feature_matrix(orders_df, traffic_df)
    ml_df = detect_ml_anomalies(feature_df)

    state.ml_anomalies = ml_df

    # -------------------------
    # Forecast + residual anomalies
    # -------------------------
    revenue_df = build_daily_revenue_series(orders_df)
    model = train_prophet_model(revenue_df)
    forecast_df = forecast_revenue(model)

    residual_df = compute_residual_anomalies(
        revenue_df,
        forecast_df
    )

    state.forecast_anomalies = residual_df
    state.forecast_full = forecast_df

    # -------------------------
    # Structured insights
    # -------------------------
    insights = generate_structured_insights(
        kpis,
        statistical_anomalies_df=stat_df,
        ml_anomalies_df=ml_df,
        forecast_residual_df=residual_df
    )

    state.insights = insights

    return state