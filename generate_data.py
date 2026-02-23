import os

from src.simulation.config import load_config
from src.simulation.utils import setup_logger, generate_date_range
from src.simulation.products import generate_products
from src.simulation.customers import generate_customers
from src.simulation.traffic import generate_traffic
from src.simulation.orders import generate_orders



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

    # -------------------------
    # Generate Products
    # -------------------------
    products_df = generate_products(config)
    logger.info("Products generated.")

    # -------------------------
    # Generate Customers
    # -------------------------
    customers_df = generate_customers(config)
    logger.info("Customers generated.")

    # -------------------------
    # Generate Website Traffic
    # -------------------------
    traffic_df = generate_traffic(config)
    logger.info("Website traffic generated.")

    traffic_df.to_csv("data/website_traffic.csv", index=False)

    # -------------------------
    # Generate Orders
    # -------------------------
    orders_df = generate_orders(config, traffic_df, products_df, customers_df)
    logger.info("Orders generated.")

    orders_df.to_csv("data/orders.csv", index=False)


    # -------------------------
    # Save to CSV
    # -------------------------
    os.makedirs("data", exist_ok=True)

    products_df.to_csv("data/products.csv", index=False)
    customers_df.to_csv("data/customers.csv", index=False)

    logger.info("Products and customers CSV files created.")

    print("Products and Customers generated successfully.")


if __name__ == "__main__":
    main()
