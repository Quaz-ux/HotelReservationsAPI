import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///./app/hotel_db.sqlite"
    SECRET_KEY = os.environ.get('HOTEL_API_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
