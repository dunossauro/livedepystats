from pytest import fixture
from app import create_app
from app.models import configure_db


@fixture
def app():
    return create_app()


@fixture
def client(app):
    app.config['TESTING'] = True
    app_context = app.test_request_context()
    app_context.push()

    with app.test_client() as client:
        with app.app_context():
            app.db.create_all()

        yield client
