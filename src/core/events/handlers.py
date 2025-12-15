from .event_bus import subscribe
from notifications.manager import send_notification

def handle_market_alert(data):
    send_notification(data)

subscribe("market_alert", handle_market_alert)
