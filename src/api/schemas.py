from pydantic import BaseModel
from typing import List


# -------------------------
# KPI Schemas
# -------------------------

class KPIResponse(BaseModel):
    total_revenue: float
    total_orders: int
    aov: float
    total_sessions: int
    conversion_rate: float


# -------------------------
# Channel Performance
# -------------------------

class ChannelPerformance(BaseModel):
    channel: str
    revenue: float
    revenue_share: float


# -------------------------
# Executive Summary
# -------------------------

class ExecutiveSummary(BaseModel):
    total_revenue: float
    conversion_rate: float
    top_channel: str
    top_channel_revenue_share: float


# -------------------------
# Conversion Analysis
# -------------------------

class ConversionAnalysis(BaseModel):
    conversion_rate: float
    conversion_status: str


# -------------------------
# Seasonality Analysis
# -------------------------

class SeasonalityAnalysis(BaseModel):
    peak_month: str
    lowest_month: str
    peak_revenue: float
    lowest_revenue: float


# -------------------------
# Anomaly Analysis
# -------------------------

class AnomalyAnalysis(BaseModel):
    statistical_anomalies: List[str]
    ml_anomalies: List[str]
    forecast_residual_anomalies: List[str]
    overlap_stat_ml: List[str]
    overlap_stat_forecast: List[str]
    overlap_ml_forecast: List[str]
    triple_overlap: List[str]


# -------------------------
# Insights Response
# -------------------------

class InsightsResponse(BaseModel):
    executive_summary: ExecutiveSummary
    channel_performance: List[ChannelPerformance]
    conversion_analysis: ConversionAnalysis
    seasonality_analysis: SeasonalityAnalysis
    anomaly_analysis: AnomalyAnalysis
    alerts: List[str]

class StatisticalAnomaly(BaseModel):
    date: str
    order_value: float
    z_score: float


class StatisticalAnomalyResponse(BaseModel):
    anomalies: List[StatisticalAnomaly]

class MLAnomaly(BaseModel):
    date: str
    order_value: float


class MLAnomalyResponse(BaseModel):
    anomalies: List[MLAnomaly]

class ForecastAnomaly(BaseModel):
    date: str
    actual_revenue: float
    predicted_revenue: float
    residual_z: float


class ForecastAnomalyResponse(BaseModel):
    anomalies: List[ForecastAnomaly]

from pydantic import BaseModel
from typing import List


class ForecastPoint(BaseModel):
    date: str
    predicted_revenue: float


class ForecastResponse(BaseModel):
    forecast: List[ForecastPoint]

class ConsensusResponse(BaseModel):
    statistical_anomalies: List[str]
    ml_anomalies: List[str]
    forecast_anomalies: List[str]
    overlap_stat_ml: List[str]
    overlap_stat_forecast: List[str]
    overlap_ml_forecast: List[str]
    triple_overlap: List[str]