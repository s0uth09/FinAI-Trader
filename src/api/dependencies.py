from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

def get_current_user(db: Session = Depends(get_db)):
    # Placeholder for auth
    if not db:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": "example"}
