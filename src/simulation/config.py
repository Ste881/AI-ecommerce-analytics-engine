import yaml
import numpy as np
from pathlib import Path
from datetime import datetime


class SimulationConfig:
    def __init__(self, config_dict):
        # -------------------------
        # General Configuration
        # -------------------------
        self.random_seed = config_dict["general"]["random_seed"]

        self.start_date = datetime.strptime(
            config_dict["general"]["start_date"], "%Y-%m-%d"
        )
        self.end_date = datetime.strptime(
            config_dict["general"]["end_date"], "%Y-%m-%d"
        )

        # -------------------------
        # Entities
        # -------------------------
        self.n_products = config_dict["entities"]["n_products"]
        self.n_customers = config_dict["entities"]["n_customers"]

        # -------------------------
        # Channels
        # -------------------------
        self.channels = config_dict["channels"]

        # Keep full raw config for future modules
        self.raw = config_dict


def load_config(path="config/simulation.yaml"):
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {path}")

    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)

    config = SimulationConfig(config_dict)

    # Set deterministic random seed
    np.random.seed(config.random_seed)

    return config
