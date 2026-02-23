# AI-Powered Autonomous E-Commerce Analytics Engine

## Overview

This project simulates a production-style internal analytics system for a mid-size D2C e-commerce company.

It is designed to demonstrate end-to-end data engineering, analytics automation, forecasting, anomaly detection and deployment architecture.

This is not a notebook project. It is a modular, production-oriented system.

---

## Business Problem

E-commerce businesses often struggle to answer:

- Why did revenue change week-over-week?
- Which acquisition channels are underperforming?
- Are there unusual traffic or revenue anomalies?
- What is the 14-day revenue forecast?
- Which products are at risk of stockout?

This engine simulates how an internal analytics team would automate those insights.

---


## Current Architecture

### Simulation Layer
- Config-driven data generation
- Product simulation with pricing & inventory
- Customer simulation
- Website traffic modeling (seasonality + growth)
- Order generation (dynamic conversion modeling)

### Analytics Layer
- KPI computation engine
- Revenue, AOV, conversion rate metrics
- Channel performance breakdown
- Monthly revenue trend analysis
- Structured LLM-ready insight generation

This system now simulates a full internal analytics pipeline:
Traffic → Orders → KPIs → Structured Insights

Next phases include:

- Product & customer simulation
- Traffic modeling with seasonality
- Marketing spend correlation
- Order generation engine
- Inventory & restocking simulation
- ETL pipeline with PostgreSQL
- Forecasting & anomaly detection
- FastAPI service layer
- Streamlit dashboard
- Docker deployment

---

## Project Structure

```
## Architecture Overview

ai_analytics_engine/
│
├── config/
│   └── simulation.yaml                # Central configuration (dates, entities, traffic, conversion, anomalies)
│
├── data/                              # Generated datasets (ignored in Git)
│   ├── products.csv
│   ├── customers.csv
│   ├── website_traffic.csv
│   └── orders.csv
│
├── logs/                              # Runtime logs (ignored in Git)
│
├── src/
│   ├── simulation/                    # Data Simulation Layer
│   │   ├── __init__.py
│   │   ├── config.py                  # YAML loader & config abstraction
│   │   ├── utils.py                   # Shared utilities (dates, logging)
│   │   ├── products.py                # Product catalog simulation
│   │   ├── customers.py               # Customer base simulation
│   │   ├── traffic.py                 # Website traffic modeling (seasonality + growth)
│   │   └── orders.py                  # Dynamic order generation (conversion modeling)
│   │
│   └── analytics/                     # Analytics & Intelligence Layer
│       ├── __init__.py
│       ├── kpis.py                    # KPI computation engine
│       └── insights_engine.py         # Structured LLM-ready insight generation
│
├── tests/                             # Unit testing layer
│   └── test_simulation_integrity.py
│
├── generate_data.py                   # Orchestration entry point (pipeline runner)
├── requirements.txt                   # Project dependencies
├── pytest.ini                         # Test configuration
└── README.md

The system is modular and layered:

1. Simulation Layer → Generates realistic business data.
2. Analytics Layer → Computes KPIs and structured insights.
3. Future Layer (Planned) → API, anomaly detection, dashboard.
```


---

## Tech Stack

- Python
- NumPy
- Pandas
- PyYAML
- Pytest
- PostgreSQL (planned)
- FastAPI (planned)
- Docker (planned)
- Structured insight engine (LLM-ready JSON output)
- Modular analytics architecture

---


