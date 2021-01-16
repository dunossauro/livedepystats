from app.serializers import EventSerial, configure_serializer
from app.models import Event


def test_configure_serial_should_exists(app):
    configure_serializer(app)


def test_event_serial_should_load_a_event_class():
    event = EventSerial().load({'event': 'zoom', 'platform': 'twitch'})

    assert isinstance(event, Event)


def test_event_serial_should_deserialize_a_json_to_class():
    event = Event(event='chorar', platform='instagram')
    dumped_event = EventSerial().dump(event)

    expected = {
        'event': 'chorar',
        'platform': 'instagram',
        'id': None,
        'created': None
    }

    assert dumped_event == expected
