from fastapi import APIRouter, Request
from src.api.schemas import InsightsResponse

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