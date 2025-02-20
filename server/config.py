import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_FILE = os.getenv("DATABASE_FILE", "sqlite:///default.db")
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_key")
    SQLALCHEMY_DATABASE_UI = f"sqlite:///{DATABASE_FILE}"
    SQLALCHEMY_TRACK_MODIFICATONS = False
    COINGECKO_API_KKEY = os.getenv("COINGECKO_API_KEY", "")
    