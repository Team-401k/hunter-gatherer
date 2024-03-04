import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    # General
    APP_NAME: str = "Omnilore Data Gathering API"
    APP_VERSION: str = "0.0.1"
    APP_DESCRIPTION: str = "API for gathering data for Omnilore's Membership Database"

    # Database
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DATABASE_ECHO = False

    # PayPal API
    PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
    PAYPAL_SECRET_KEY = os.getenv("PAYPAL_SECRET_KEY")

    # Stripe API
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

    # SquareSpace API
    SQUARESPACE_API_KEY = os.getenv("SQUARESPACE_API_KEY")
    

    HOST = "localhost"
    PORT = 8000


settings = Settings()
