import pandas as pd


def compute_kpis(orders_df, traffic_df):
    results = {}

    # Total Revenue
    total_revenue = orders_df["order_value"].sum()
    results["total_revenue"] = total_revenue

    # Total Orders
    total_orders = len(orders_df)
    results["total_orders"] = total_orders

    # Average Order Value
    results["aov"] = total_revenue / total_orders if total_orders > 0 else 0

    # Total Sessions
    total_sessions = traffic_df["sessions"].sum()
    results["total_sessions"] = total_sessions

    # Conversion Rate
    results["conversion_rate"] = total_orders / total_sessions

    # Revenue by Channel
    revenue_by_channel = (
        orders_df.groupby("channel")["order_value"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )
    results["revenue_by_channel"] = revenue_by_channel

    # Orders by Channel
    orders_by_channel = (
        orders_df.groupby("channel")
        .size()
        .sort_values(ascending=False)
        .to_dict()
    )
    results["orders_by_channel"] = orders_by_channel

    # Monthly Revenue Trend
    orders_df["month"] = pd.to_datetime(orders_df["order_date"]).dt.to_period("M")
    monthly_revenue = (
        orders_df.groupby("month")["order_value"]
        .sum()
        .to_dict()
    )
    results["monthly_revenue"] = monthly_revenue

    return results