from flask import Flask
from app import create_app

"""
Lista de eventos:

- Chá
- Zoom
- Cigarrinho
- Gritinho do MJ
- Poesia
- Violão
- Palmas
- Beijo
- Chorar
- Bebê
- Porre
"""


def test_create_app_should_return_a_flask_app():
    """
    Testa se o factory (create_app) retorna
      uma instancia de Flask.
    """
    assert isinstance(create_app(), Flask)


def test_sqlalchemy_configuration_should_be_defined(app):
    """
    Dado que exista a aplicação
    Então 'SQLALCHEMY_DATABASE_URI' deve estar na configuração
    """
    assert 'SQLALCHEMY_DATABASE_URI' in app.config
