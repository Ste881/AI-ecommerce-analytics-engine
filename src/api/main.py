from fastapi import FastAPI
from src.api.state import load_and_compute_state
from src.api.routes import health
from src.api.routes import analytics


app = FastAPI(
    title="AI E-Commerce Analytics Engine API",
    description="Production-style analytics backend with KPI computation, multi-model anomaly detection, and forecasting.",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    app.state.analytics = load_and_compute_state()


app.include_router(health.router)
app.include_router(analytics.router)