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

## Current Phase

- Config-driven simulation foundation  
- Deterministic random seed  
- Modular architecture  
- Logging system  
- Pytest testing framework  

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

ai_analytics_engine /
│
├── config /
├── src/

│ ├── simulation/

│ └── validators/

├── tests/
├── generate_data.py
├── requirements.txt
├── pytest.ini
└── README.md


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

---


