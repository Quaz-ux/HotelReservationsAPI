from sqlalchemy import Column, Integer, Float

from . import Base


class Room(Base):
    room_number = Column(Integer, unique=True)
    floor = Column(Integer)
    people_capacity = Column(Integer)
    price_per_night = Column(Float)