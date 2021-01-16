from flask_marshmallow import Marshmallow
from .models import Event

ma = Marshmallow()


def configure_serializer(app):
    ma.init_app(app)


class EventSerial(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True
