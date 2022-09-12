from flask import jsonify, Blueprint
from flask_login import logout_user, current_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/api/user/login")
def user_login():
    if current_user.is_authenticated:
        return jsonify({'massage': 'You are logged in!'})

    return jsonify({'ping': "Pong"})

@user_routes.route("/api/user/logout")
def user_logout():
    logout_user()
    return jsonify({'massage': 'Logged out.'})