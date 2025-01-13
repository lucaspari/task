from flask import Flask
from app.routes import user_routes
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes)
    return app