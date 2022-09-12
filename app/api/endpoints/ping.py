from flask import jsonify, Blueprint

ping_routes = Blueprint("ping_routes", __name__)

@ping_routes.route("/api/ping")
def ping():
    return jsonify({'ping': "Pong"})

