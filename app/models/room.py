from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    people_capacity = db.Column(db.Integer)
    price_per_night = db.Column(db.Float)