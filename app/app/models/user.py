from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from . import Base
from .. import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, Base):
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(100), nullable=False, unique=True)