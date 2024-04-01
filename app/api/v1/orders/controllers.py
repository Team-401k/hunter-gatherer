"""API Route handlers for orders."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.external_apis.schemas import OrdersResponse
from app.api.v1.orders.models import Order
from app.api.v1.orders import services
from app.api.v1.users.models import User
from app.database import db
from app.api.v1.external_apis.pp_api import PayPalAPI
from app.api.v1.external_apis.stripe_api import StripeAPI
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI


router = APIRouter()



@router.post("/sqsp_ingestion")
def ingest_sqsp_orders(session: Session = Depends(db)):
    """Write documentation here."""

    # order = Order(
    #    purchase_id=1,
    #     user_id=1,
    #     amount=1.0,
    #     date='2024-03-27 16:29:47.522126',
    #     type='type',
    #     method='method',
    #     fee=1.0,
    #     stripe_paypal_id='stripe_paypal_id',
    # )
    sqsp_orders: OrdersResponse = services.get_orders(services.OrderService.SQSP, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
    # ping api
    # api returns list of pydantic objects
    for item in sqsp_orders.result:
        line_items_size = len(item.lineItems)
        if line_items_size > 1: 
            new_order = Order(
                purchase_id=item.id,
                amount=item.grandTotal.value,
                date=item.createdOn,
                type='sqsp',
                method='method',
                fee=0.0,
                stripe_paypal_id=None,
            )
            # session.add(new_order)
            # session.commit()  
            for i in range(line_items_size):
                if 'forum' in item.lineItems[i].productName.lower():
                    new_user = User(
                        email=item.customerEmail,
                        name=item.billingAddress.firstName + item.billingAddress.lastName,
                        address=item.billingAddress.address1 + item.billingAddress.address2,
                    )
                    session.add(new_user)
                    session.commit()
                elif 'membership' in item.lineItems[i].productName.lower():
                    new_user = User(
                        email=item.customerEmail,
                        name=item.billingAddress.name,
                        address=item.billingAddress.address1 + item.billingAddress.address2,
                    )
                    session.add(new_user)
                    session.commit()
                    



        """

    email=Column(String, nullable=False, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    date_joined = Column(DateTime)
    date_renewed = Column(DateTime)
    is_member = Column(Boolean)
        
        """



        
        # break


@router.post("/stripe_ingestion")
def ingest_stripe_orders(session: Session = Depends(db)):
    stripe_orders = services.get_orders(services.OrderService.STRIPE, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
    for item in stripe_orders:
        new_order = Order(**item.model_dump())
        session.add(new_order)
        session.commit()


@router.post("/paypal_ingestion")
def ingest_pp_orders(session: Session = Depends(db)):
    pp_orders = services.get_orders(services.OrderService.PAYPAL, '2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
    for item in pp_orders:
        new_order = Order(**item.model_dump())
        session.add(new_order)
        session.commit()


