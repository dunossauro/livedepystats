from logging import getLogger
from flask import Flask
from config import get_env
from .models import configure_db
from .serializers import configure_serializer
from .api import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_env())
    gunicorn_logger = getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    configure_db(app)
    configure_serializer(app)

    app.register_blueprint(api)
    return app
