from flask import Flask
from app.routes import api
from app.db import init_db
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs("instance", exist_ok=True)
    init_db()

    app.register_blueprint(api)

    return app
