import pandas as pd
import numpy as np


def generate_traffic(config):
    # Create date range
    dates = pd.date_range(config.start_date, config.end_date, freq="D")

    # Create base DataFrame
    df = pd.DataFrame({"date": dates})

    # Extract date features
    df["day_of_week"] = df["date"].dt.weekday
    df["month"] = df["date"].dt.month

    # Weekend multiplier
    weekend_multiplier = np.where(
        df["day_of_week"] >= 5,
        config.raw["traffic"]["weekend_multiplier"],
        1.0
    )

    # Monthly growth multiplier
    monthly_growth_rate = config.raw["traffic"]["monthly_growth_rate"]
    month_multiplier = 1 + (df["month"] - 1) * monthly_growth_rate

    df["multiplier"] = weekend_multiplier * month_multiplier

    # Expand across channels (Cartesian join)
    channels_df = pd.DataFrame({"channel": config.channels})

    df = df.merge(channels_df, how="cross")

    # Base sessions per channel
    base_sessions_map = config.raw["traffic"]["base_sessions"]

    df["base_sessions"] = df["channel"].map(base_sessions_map)

    # Add controlled randomness
    noise = np.random.normal(1.0, 0.05, size=len(df))

    df["sessions"] = (
        df["base_sessions"]
        * df["multiplier"]
        * noise
    ).clip(lower=0).astype(int)

    # Final cleanup
    df = df[["date", "channel", "sessions"]]

    return df
