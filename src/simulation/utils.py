import pandas as pd
import logging
import os


def generate_date_range(start_date, end_date):
    return pd.date_range(start=start_date, end=end_date, freq="D")


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/simulation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    return logging.getLogger(__name__)
