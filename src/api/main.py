from fastapi import FastAPI
from api.routers import market, analysis, alerts, webhooks, subscriptions
from api.middleware import add_middleware

app = FastAPI(title="FinAI Trader API")

add_middleware(app)

app.include_router(market.router, prefix="/market")
app.include_router(analysis.router, prefix="/analysis")
app.include_router(alerts.router, prefix="/alerts")
app.include_router(webhooks.router, prefix="/webhooks")
app.include_router(subscriptions.router, prefix="/subscriptions")

@app.get("/")
def root():
    return {"message": "FinAI Trader API"}
