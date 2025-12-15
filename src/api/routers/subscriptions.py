from fastapi import APIRouter
from subscription.billing import create_subscription

router = APIRouter()

@router.post("/subscribe")
def subscribe(plan: str):
    return create_subscription(plan)
