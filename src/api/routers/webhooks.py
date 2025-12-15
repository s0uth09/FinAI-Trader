from fastapi import APIRouter, Request
from subscription.webhooks import handle_stripe_webhook

router = APIRouter()

@router.post("/stripe")
async def stripe_webhook(request: Request):
    return await handle_stripe_webhook(request)
