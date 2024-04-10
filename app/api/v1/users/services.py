"""Services for users."""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.api.v1.users.models import User


def get_user_by_pk(session: Session, name: str, email: str):
    return session.query(User).filter(User.pk == f"{name}_{email}").first()


def create_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    first_joined: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
    date_renewed: Optional[datetime] = None,
):
    new_user = User(
        pk=f"{name}_{email}",
        email=email,
        name=name,
        address=address,
        phone=phone,
        emergency_contact=emergency_contact,
        emergency_contact_phone=emergency_contact_phone,
        is_member=is_member,
        first_joined=first_joined,
        date_expired=date_expired,
        date_renewed=date_renewed,
    )
    return new_user


def upsert_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    date_renewed: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
):
    user = get_user_by_pk(session, name, email)
    if user:
        # since already exists, update date_renewed not first_joined
        if name:
            user.name = name
        if address:
            user.address = address
        if phone:
            user.phone = phone
        if email:
            user.email = email
        if is_member:
            user.is_member = is_member
        if date_renewed:
            user.date_renewed = date_renewed
        if date_expired:
            user.date_expired = date_expired
        if emergency_contact:
            user.emergency_contact = emergency_contact
        if emergency_contact_phone:
            user.emergency_contact_phone = emergency_contact_phone
    else:
        # notice passing in date_renewed to first_joined because since this user doesn't exist, date_renewed is the actual join date
        user = create_user(
            session,
            email=email,
            name=name,
            address=address,
            phone=phone,
            emergency_contact=emergency_contact,
            emergency_contact_phone=emergency_contact_phone,
            is_member=is_member,
            first_joined=date_renewed,
            date_expired=date_expired,
            date_renewed=date_renewed,
        )
    session.add(user)
    session.flush()
    session.refresh(user)
    return user
