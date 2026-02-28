from fastapi import APIRouter, Request
from src.api.schemas import InsightsResponse
from src.api.schemas import KPIResponse

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