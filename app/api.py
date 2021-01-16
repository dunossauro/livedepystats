from flask import Blueprint, request, current_app
from .serializers import EventSerial

api = Blueprint('api', __name__)


@api.route('/event', methods=['POST'])
def event():
    es = EventSerial()
    event = es.load(request.json)

    current_app.db.session.add(event)
    current_app.db.session.commit()

    return es.dump(event), 201
