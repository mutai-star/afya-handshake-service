from flask import Blueprint, jsonify
from app.services import initiate_handshake, complete_handshake

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return "Afya Handshake Service Running"

@api.route("/initiate")
def initiate():
    return jsonify(initiate_handshake())

@api.route("/complete")
def complete():
    return jsonify(complete_handshake())

@api.route("/auto")
def auto():
    init = initiate_handshake()
    if not init.get("success"):
        return jsonify(init), 400

    return jsonify(complete_handshake())
