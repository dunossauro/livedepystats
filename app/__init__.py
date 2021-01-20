from logging import getLogger
from flask import Flask
from flask.logging import default_handler
from .models import configure_db
from .serializers import configure_serializer
from .api import api


def create_app():
    app = Flask(__name__)

    root = getLogger()
    gunicorn_logger = getLogger('gunicorn.debug')
    root.addHandler(default_handler)
    root.addHandler(gunicorn_logger)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)
    configure_serializer(app)

    app.register_blueprint(api)
    return app
