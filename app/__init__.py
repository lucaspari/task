from flask import Flask
from app.routes import user_routes
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes)
    CORS(app)
    return app