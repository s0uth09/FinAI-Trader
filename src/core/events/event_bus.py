from typing import Callable, Dict

event_handlers: Dict[str, Callable] = {}

def subscribe(event_type: str, handler: Callable):
    event_handlers[event_type] = handler

def publish(event_type: str, data: dict):
    if event_type in event_handlers:
        event_handlers[event_type](data)
