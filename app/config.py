import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///hotel_db.sqlite"
    SECRET_KEY = os.environ.get('HOTEL_API_SECRET_KEY')