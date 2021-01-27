from os import environ

postgres_uri = 'postgresql://{user}:{pass}@{host}:{port}/{db}'


class Base:
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class Testing(Base):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    DEBUG = True


class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_uri.format(
        'database',
        'batatinha',
        'localhost',
        '5432',
        'livedepystats'
    )


class Production(Base):
    SQLALCHEMY_DATABASE_URI = postgres_uri.format(
        'database',
        'batatinha',
        'localhost',
        '5432',
        'livedepystats'
    )


envs = {
    'base': Base,
    'testing': Testing,
    'development': Development,
    'production': Production
}


def get_env():
    return envs[environ.get('FLASK_ENV', default='production')]
