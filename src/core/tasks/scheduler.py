from celery import Celery
from config.settings import settings

app = Celery("tasks", broker=settings.celery_broker_url)

@app.task
def schedule_analysis():
    # Placeholder
    pass
