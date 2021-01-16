from flask import Flask
from .models import configure_db
from .serializers import configure_serializer
from .api import api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)
    configure_serializer(app)

    app.register_blueprint(api)
    return app
