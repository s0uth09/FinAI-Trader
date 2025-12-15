from fastapi import APIRouter
from ai.models.grok.analyzer import analyze_market

router = APIRouter()

@router.post("/analyze")
def perform_analysis(data: dict):
    return analyze_market(data)
