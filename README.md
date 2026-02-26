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
- Are unusual revenue spikes real or noise?
- Are anomalies confirmed across multiple models?
- What is the forward-looking revenue forecast?
- Is actual revenue deviating from expected forecast behavior?

This engine simulates how an internal analytics team would automate intelligence, monitoring, and anomaly confirmation.

---

## Current Architecture

### Simulation Layer

- Config-driven data generation
- Product simulation (pricing, cost, inventory)
- Customer base simulation
- Website traffic modeling (seasonality + monthly growth)
- Dynamic conversion modeling (channel bias + seasonal variation)
- Revenue shock injection (flash sale, outage simulation)
- Deterministic random seed for reproducibility

### Analytics Layer

- KPI computation engine
- Revenue, AOV, conversion rate metrics
- Channel performance breakdown
- Monthly revenue trend analysis
- Structured LLM-ready insight generation

### Anomaly Detection Systems

- Statistical anomaly detection (rolling mean + z-score)
- ML anomaly detection (Isolation Forest with engineered daily features)
- Forecast residual anomaly detection (Prophet-based time-series modeling)
- Multi-model anomaly consensus logic (pairwise + triple overlap confirmation)

This system now simulates a full internal analytics intelligence pipeline:

Traffic → Orders → KPIs → Anomaly Detection → Forecasting → Structured Insights

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
│   │   └── orders.py                  # Dynamic order generation (conversion modeling + event injection)
│   │
│   └── analytics/                     # Analytics & Intelligence Layer
│       ├── __init__.py
│       ├── kpis.py                    # KPI computation engine
│       ├── anomaly_detection.py       # Statistical anomaly detection (rolling z-score)
│       ├── ml_anomaly_detection.py    # Isolation Forest anomaly detection
│       ├── forecasting.py             # Prophet forecasting + residual anomaly detection
│       └── insights_engine.py         # Structured LLM-ready insight generation + anomaly consensus logic
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
2. Analytics Layer → Computes KPIs, anomalies, forecasts, and structured insights.
3. Multi-Model Consensus Layer → Confirms anomalies across statistical, ML, and forecasting systems.
4. Future Layer (Planned) → API service, database integration, dashboard, Dockerization.

```

---

## Tech Stack

- Python
- NumPy
- Pandas
- PyYAML
- Prophet (Time-Series Forecasting)
- Scikit-learn (Isolation Forest)
- Pytest
- Structured LLM-ready JSON insight engine
- Modular analytics architecture

---

## Planned Infrastructure:

- FastAPI
- PostgreSQL
- Docker
- Streamlit Dashboard
