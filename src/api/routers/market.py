from fastapi import APIRouter, Depends
from data.clients.binance import get_market_data

router = APIRouter()

@router.get("/data")
def fetch_market(symbol: str):
    return get_market_data(symbol)
