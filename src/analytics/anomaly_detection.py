import pandas as pd
import numpy as np


def detect_statistical_anomalies(df, value_column, date_column="date", window=14, z_threshold=2.5):
    """
    Detect anomalies using rolling mean and rolling standard deviation.

    Parameters:
        df (DataFrame): Data containing time series.
        value_column (str): Column to evaluate.
        date_column (str): Date column.
        window (int): Rolling window size.
        z_threshold (float): Z-score threshold for anomaly.

    Returns:
        DataFrame with anomaly flags.
    """

    data = df.copy()
    data[date_column] = pd.to_datetime(data[date_column])
    data = data.sort_values(date_column)

    data["rolling_mean"] = data[value_column].rolling(window=window).mean()
    data["rolling_std"] = data[value_column].rolling(window=window).std()

    data["z_score"] = (
        (data[value_column] - data["rolling_mean"]) /
        data["rolling_std"]
    )

    data["is_anomaly"] = data["z_score"].abs() > z_threshold

    return data