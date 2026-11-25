from flask import Flask 
from app.config import config_by_name
from app.router import bp 


def create_app(config_name: str | None = None) -> Flask: 
    app = Flask(__name__)
    name = config_name or "development"
    app.config.from_object(config_by_name[name])
    app.register_blueprint(bp)
    return app 

