from flask import jsonify, Blueprint, request
from flask_login import logout_user, current_user

from app import bcrypt, db
from app.models import User

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/api/user/login", methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:
        return jsonify({'massage': 'You are logged in!'})

    data = request.json
    username = request.json('username')
    password = request.json('password')
    # user = User.querry.get(username=username)
    user = db.querry(User).get(User.username == username)
    print(user.username)

    return jsonify({'ping': "Pong"})

@user_routes.route("/api/user/create")
def user_create():

    user = User(username="admin", password=bcrypt.generate_password_hash("admin"))
    db.session.add(user)
    db.session.commit()
    print(user.username)

    return jsonify({'ping': "Pong"})

@user_routes.route("/api/user/logout")
def user_logout():
    logout_user()
    return jsonify({'massage': 'Logged out.'})