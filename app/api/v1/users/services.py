"""Services for users."""

from typing import Optional

from sqlalchemy.orm import Session

from app.api.v1.users.models import User


def get_user_by_email(session: Session, email: str):
    return session.query(User).filter(User.email == email).first()


def create_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
):
    new_user = User(
        email=email,
        name=name,
        address=address,
        phone=phone,
        emergency_contact=emergency_contact,
        emergency_contact_phone=emergency_contact_phone,
    )
    return new_user


def upsert_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
):
    user = get_user_by_email(session, email)
    if user:
        if not user.name and name:
            user.name = name
        if not user.address and address:
            user.address = address
        if not user.phone and phone:
            user.phone = phone
        if not user.emergency_contact and emergency_contact:
            user.emergency_contact = emergency_contact
        if not user.emergency_contact_phone and emergency_contact_phone:
            user.emergency_contact_phone = emergency_contact_phone
    else:
        user = create_user(
            session,
            email=email,
            name=name,
            address=address,
            phone=phone,
            emergency_contact=emergency_contact,
            emergency_contact_phone=emergency_contact_phone,
        )
    session.add(user)
    session.flush()
    session.refresh(user)
    return user
