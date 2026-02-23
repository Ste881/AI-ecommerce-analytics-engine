import numpy as np
import pandas as pd


def generate_orders(config, traffic_df, products_df, customers_df):
    df = traffic_df.copy()

    base_rate = config.raw["conversion"]["base_rate"]
    seasonal_variation = config.raw["conversion"]["seasonal_variation"]

    # Monthly seasonality using sine wave
    df["month"] = pd.to_datetime(df["date"]).dt.month
    df["seasonality"] = seasonal_variation * np.sin(2 * np.pi * df["month"] / 12)

    # Channel bias
    channel_bias = {
        "Organic": 0.005,
        "Paid_Search": 0.002,
        "Paid_Social": -0.003,
        "Email": 0.008
    }

    df["channel_bias"] = df["channel"].map(channel_bias)

    # Random noise
    noise = np.random.normal(0, 0.002, size=len(df))

    # Final conversion rate
    df["conversion_rate"] = (
        base_rate
        + df["seasonality"]
        + df["channel_bias"]
        + noise
    ).clip(lower=0)

    # Orders count
    df["orders"] = (df["sessions"] * df["conversion_rate"]).astype(int)

    # Expand rows to order-level
    order_rows = []

    product_ids = products_df["product_id"].values
    product_prices = dict(zip(products_df["product_id"], products_df["unit_price"]))

    customer_ids = customers_df["customer_id"].values

    for _, row in df.iterrows():
        for _ in range(row["orders"]):
            product_id = np.random.choice(product_ids)
            customer_id = np.random.choice(customer_ids)

            order_rows.append({
                "order_date": row["date"],
                "channel": row["channel"],
                "product_id": product_id,
                "customer_id": customer_id,
                "order_value": product_prices[product_id]
            })

    orders_df = pd.DataFrame(order_rows)

    return orders_df