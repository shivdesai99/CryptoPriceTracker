import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_key")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getenv('DATABASE_FILE', 'default.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "")
