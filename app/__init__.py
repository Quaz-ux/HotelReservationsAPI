from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.api.endpoints.ping import ping_routes
from app.api.endpoints.user import user_routes
from app.models.room import Room
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(ping_routes)
    app.register_blueprint(user_routes)
    return app