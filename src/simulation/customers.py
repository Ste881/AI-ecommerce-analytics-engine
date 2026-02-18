import pandas as pd
import numpy as np


CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
]


def generate_customers(config):
    n_customers = config.n_customers

    customer_ids = np.arange(1, n_customers + 1)

    signup_dates = pd.to_datetime(
        np.random.choice(
            pd.date_range("2023-01-01", config.start_date),
            size=n_customers
        )
    )

    cities = np.random.choice(CITIES, size=n_customers)

    df = pd.DataFrame({
        "customer_id": customer_ids,
        "signup_date": signup_dates,
        "city": cities,
    })

    return df
