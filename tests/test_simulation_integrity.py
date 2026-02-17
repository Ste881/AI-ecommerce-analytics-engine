from src.simulation.config import load_config
from src.simulation.utils import generate_date_range


def test_config_loading():
    config = load_config()
    assert config.n_products > 0
    assert config.n_customers > 0
    assert len(config.channels) > 0


def test_date_range():
    config = load_config()
    dates = generate_date_range(config.start_date, config.end_date)
    assert len(dates) == 365
