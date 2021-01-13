from pytest import fixture
from app import create_app


@fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app_context = app.test_request_context()
    app_context.push()

    with app.test_client() as client:
        yield client
