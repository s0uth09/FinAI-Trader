from fastapi import FastAPI
import logging

def add_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request, call_next):
        logging.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        return response
