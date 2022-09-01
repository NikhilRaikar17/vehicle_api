from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")
    SWAGGER_URL = '/api'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "IONOS-API"
        }
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
        from application.vehicle import vehicle_api_blueprint
        app.register_blueprint(vehicle_api_blueprint)
        return app