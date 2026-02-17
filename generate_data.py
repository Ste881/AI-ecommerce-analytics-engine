from src.simulation.config import load_config
from src.simulation.utils import setup_logger, generate_date_range


def main():
    # Load configuration
    config = load_config()

    # Setup logging
    logger = setup_logger()
    logger.info("Simulation started.")

    # Generate date range
    dates = generate_date_range(config.start_date, config.end_date)

    print("=" * 60)
    print("AI E-Commerce Data Simulation Engine")
    print("=" * 60)
    print(f"Start Date: {config.start_date.date()}")
    print(f"End Date: {config.end_date.date()}")
    print(f"Total Days: {len(dates)}")
    print(f"Number of Products: {config.n_products}")
    print(f"Number of Customers: {config.n_customers}")
    print(f"Channels: {config.channels}")
    print("=" * 60)

    logger.info(f"Generated {len(dates)} simulation days.")
    logger.info("Initialization complete.")


if __name__ == "__main__":
    main()
