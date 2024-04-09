"""Services for users."""

from typing import Optional

from sqlalchemy.orm import Session

from app.api.v1.users.models import User

from datetime import datetime


def get_user_by_pk(session: Session, name: str, email: str):
    return session.query(User).filter(User.pk == f"{name}_{email}").first()


def create_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    first_joined: Optional[datetime],
    date_expired: Optional[datetime],
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False
):
    new_user = User(
        pk=f"{name}_{email}",
        email=email,
        name=name,
        address=address,
        phone=phone,
        emergency_contact=emergency_contact,
        emergency_contact_phone=emergency_contact_phone,
        is_member = is_member,
        first_joined = first_joined,
        date_expired = date_expired,

    )
    return new_user


def upsert_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    date_renewed: Optional[datetime],
    date_expired: Optional[datetime],
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
):
    user = get_user_by_pk(session, name, email)
    if user:
        #since already exists, update date_renewed not first_joined
        user.name = name
        user.address = address
        user.phone = phone
        user.email = email
        user.is_member = is_member
        user.date_renewed = date_renewed
        user.date_expired = date_expired
        user.emergency_contact = emergency_contact
        user.emergency_contact_phone = emergency_contact_phone
    else:
        #notice passing in date_renewed to first_joined because since this user doesn't exist, date_renewed is the actual join date
        user = create_user(
            session,
            email=email,
            name=name,
            address=address,
            phone=phone,
            emergency_contact=emergency_contact,
            emergency_contact_phone=emergency_contact_phone,
            is_member = is_member,
            first_joined = date_renewed,
            date_expired = date_expired,
        )
    session.add(user)
    session.flush()
    session.refresh(user)
    return user
