from sqlalchemy.orm import Session
from .models import User

def create_user(db: Session, email: str):
    user = User(email=email)
    db.add(user)
    db.commit()
    return user
