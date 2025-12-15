from fastapi import APIRouter
from notifications.manager import send_alert

router = APIRouter()

@router.post("/set")
def set_alert(params: dict):
    send_alert(params)
    return {"status": "alert set"}
