from fastapi import APIRouter, Request
from src.api.schemas import InsightsResponse
from src.api.schemas import KPIResponse
from src.api.schemas import StatisticalAnomalyResponse
from src.api.schemas import MLAnomalyResponse
from src.api.schemas import ForecastAnomalyResponse
import pandas as pd
from fastapi import Query
from src.api.schemas import ForecastResponse, ForecastPoint
from fastapi import APIRouter, Request, Query



router = APIRouter()


@router.get("/insights", response_model=InsightsResponse)
def get_insights(request: Request):
    """
    Returns structured analytics insights including:
    - Executive summary
    - Channel performance
    - Conversion analysis
    - Seasonality analysis
    - Multi-model anomaly analysis
    - Alerts
    """
    return request.app.state.analytics.insights

@router.get("/kpis", response_model=KPIResponse)
def get_kpis(request: Request):
    """
    Returns top-level KPI summary.
    """
    return request.app.state.analytics.kpis

@router.get("/anomalies/statistical", response_model=StatisticalAnomalyResponse)
def get_statistical_anomalies(request: Request):
    df = request.app.state.analytics.stat_anomalies

    filtered = df[df["is_anomaly"]]

    results = [
        {
            "date": str(row["date"]),
            "order_value": float(row["order_value"]),
            "z_score": float(row["z_score"])
        }
        for _, row in filtered.iterrows()
    ]

    return {"anomalies": results}

@router.get("/anomalies/ml", response_model=MLAnomalyResponse)
def get_ml_anomalies(request: Request):
    df = request.app.state.analytics.ml_anomalies

    filtered = df[df["ml_anomaly_flag"]]

    results = [
        {
            "date": str(row["date"]),
            "order_value": float(row["order_value"])
        }
        for _, row in filtered.iterrows()
    ]

    return {"anomalies": results}

@router.get("/anomalies/forecast", response_model=ForecastAnomalyResponse)
def get_forecast_anomalies(request: Request):
    df = request.app.state.analytics.forecast_anomalies

    filtered = df[df["residual_anomaly_flag"]]

    results = [
        {
            "date": str(row["ds"]),
            "actual_revenue": float(row["y"]),
            "predicted_revenue": float(row["yhat"]),
            "residual_z": float(row["residual_z"])
        }
        for _, row in filtered.iterrows()
    ]

    return {"anomalies": results}

@router.get("/forecast", response_model=ForecastResponse)
def get_forecast(request: Request, days: int = Query(14, ge=1, le=90)):

    forecast_df = request.app.state.analytics.forecast_full
    forecast_residual_df = request.app.state.analytics.forecast_anomalies

    # Last actual historical date
    last_actual_date = forecast_residual_df["ds"].max()

    # Select strictly future rows
    future_df = forecast_df[forecast_df["ds"] > last_actual_date]

    forecast_points = [
        ForecastPoint(
            date=row["ds"].strftime("%Y-%m-%d"),
            predicted_revenue=float(row["yhat"])
        )
        for _, row in future_df.head(days).iterrows()
    ]

    return ForecastResponse(forecast=forecast_points)