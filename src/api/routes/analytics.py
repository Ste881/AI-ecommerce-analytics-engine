from fastapi import APIRouter, Request
from src.api.schemas import InsightsResponse
from src.api.schemas import KPIResponse
from src.api.schemas import StatisticalAnomalyResponse


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