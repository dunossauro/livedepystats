from pytest import mark
from app.models import configure_db, Event


def test_configure_db_should_create_app_db(app):
    configure_db(app)
    assert hasattr(app, 'db')


@mark.parametrize('attr', ['id', 'event', 'platform', 'created'])
def test_check_event_table_attributes(attr):
    assert hasattr(Event, attr)
