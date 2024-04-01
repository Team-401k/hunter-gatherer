"""Services for users."""
from sqlalchemy.orm import Session

from app.api.v1.users.models import User

def get_user_by_email(session: Session, email: str):
    return session.query(User).filter(User.email == email).first()