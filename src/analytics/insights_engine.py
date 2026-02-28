def generate_structured_insights(
    kpis: dict,
    statistical_anomalies_df=None,
    ml_anomalies_df=None,
    forecast_residual_df=None
):
    insights = {}

    total_revenue = float(kpis["total_revenue"])
    conversion_rate = float(kpis["conversion_rate"])
    revenue_by_channel = {
        k: float(v) for k, v in kpis["revenue_by_channel"].items()
    }
    monthly_revenue = {
        str(k): float(v) for k, v in kpis["monthly_revenue"].items()
    }

    # -------- Executive Summary --------
    best_channel = max(revenue_by_channel, key=revenue_by_channel.get)
    best_channel_share = revenue_by_channel[best_channel] / total_revenue

    insights["executive_summary"] = {
        "total_revenue": round(total_revenue, 2),
        "conversion_rate": round(conversion_rate, 4),
        "top_channel": best_channel,
        "top_channel_revenue_share": round(best_channel_share, 4),
    }

    # -------- Channel Performance --------
    channel_analysis = []
    for channel, revenue in revenue_by_channel.items():
        share = revenue / total_revenue
        channel_analysis.append({
            "channel": channel,
            "revenue": round(revenue, 2),
            "revenue_share": round(share, 4)
        })

    insights["channel_performance"] = sorted(
        channel_analysis,
        key=lambda x: x["revenue"],
        reverse=True
    )

    # -------- Conversion Analysis --------
    if conversion_rate > 0.03:
        conversion_status = "High"
    elif conversion_rate > 0.02:
        conversion_status = "Healthy"
    else:
        conversion_status = "Low"

    insights["conversion_analysis"] = {
        "conversion_rate": round(conversion_rate, 4),
        "conversion_status": conversion_status
    }

    # -------- Seasonality Analysis --------
    months = list(monthly_revenue.keys())
    values = list(monthly_revenue.values())

    peak_month = months[values.index(max(values))]
    lowest_month = months[values.index(min(values))]

    insights["seasonality_analysis"] = {
        "peak_month": peak_month,
        "lowest_month": lowest_month,
        "peak_revenue": round(max(values), 2),
        "lowest_revenue": round(min(values), 2)
    }

        # -------- Anomaly Analysis --------
    anomaly_analysis = {
        "statistical_anomalies": [],
        "ml_anomalies": [],
        "forecast_residual_anomalies": [],
        "overlap_stat_ml": [],
        "overlap_stat_forecast": [],
        "overlap_ml_forecast": [],
        "triple_overlap": []
    }

    stat_days = []
    ml_days = []
    forecast_days = []

    if statistical_anomalies_df is not None:
        stat_days = statistical_anomalies_df[
            statistical_anomalies_df["is_anomaly"]
        ]["date"].astype(str).tolist()
        anomaly_analysis["statistical_anomalies"] = stat_days

    if ml_anomalies_df is not None:
        ml_days = ml_anomalies_df[
            ml_anomalies_df["ml_anomaly_flag"]
        ]["date"].astype(str).tolist()
        anomaly_analysis["ml_anomalies"] = ml_days

    if forecast_residual_df is not None:
        forecast_days = forecast_residual_df[
            forecast_residual_df["residual_anomaly_flag"]
        ]["ds"].astype(str).tolist()
        anomaly_analysis["forecast_residual_anomalies"] = forecast_days

    stat_set = set(stat_days)
    ml_set = set(ml_days)
    forecast_set = set(forecast_days)

    anomaly_analysis["overlap_stat_ml"] = list(stat_set.intersection(ml_set))
    anomaly_analysis["overlap_stat_forecast"] = list(stat_set.intersection(forecast_set))
    anomaly_analysis["overlap_ml_forecast"] = list(ml_set.intersection(forecast_set))
    anomaly_analysis["triple_overlap"] = list(
        stat_set.intersection(ml_set).intersection(forecast_set)
    )

    insights["anomaly_analysis"] = anomaly_analysis

    # -------- Alerts --------
    alerts = []

    if best_channel_share > 0.6:
        alerts.append("Revenue concentration risk: over 60% revenue from single channel.")

    if conversion_rate < 0.02:
        alerts.append("Conversion rate below expected baseline.")

    if len(anomaly_analysis["triple_overlap"]) > 0:
        alerts.append("Critical anomaly confirmed by statistical, ML, and forecasting models.")

    elif len(anomaly_analysis["overlap_stat_ml"]) > 0:
        alerts.append("High-confidence anomaly detected by statistical and ML models.")

    elif len(forecast_days) > 0:
        alerts.append("Forecast-based revenue deviation detected.")

    insights["alerts"] = alerts

    return insights