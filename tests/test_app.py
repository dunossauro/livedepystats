from flask import Flask
from app import create_app


def test_create_app_should_return_a_flask_app():
    """
    Testa se o factory (create_app) retorna
      uma instancia de Flask.
    """
    assert isinstance(create_app(), Flask)
