import pandas as pd
import numpy as np


CATEGORIES = ["Apparel", "Electronics", "Beauty", "Home", "Accessories"]


def generate_products(config):
    n_products = config.n_products

    product_ids = np.arange(1, n_products + 1)

    categories = np.random.choice(CATEGORIES, size=n_products)

    # Category-based pricing
    price_ranges = {
        "Apparel": (500, 3000),
        "Electronics": (2000, 20000),
        "Beauty": (300, 2500),
        "Home": (800, 10000),
        "Accessories": (200, 1500),
    }

    prices = []
    cost_prices = []
    demand_weights = []

    for category in categories:
        low, high = price_ranges[category]
        price = np.random.uniform(low, high)
        margin = np.random.uniform(0.3, 0.6)  # 30–60% margin
        cost_price = price * (1 - margin)

        prices.append(round(price, 2))
        cost_prices.append(round(cost_price, 2))
        demand_weights.append(np.random.uniform(0.5, 2.0))

    df = pd.DataFrame({
        "product_id": product_ids,
        "category": categories,
        "unit_price": prices,
        "cost_price": cost_prices,
        "demand_weight": demand_weights,
        "stock_level": np.random.randint(200, 1000, size=n_products),
    })

    return df
