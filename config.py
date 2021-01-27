from os import environ

postgres_uri = 'postgresql://{user}:{passw}@{host}:{port}/{db}'


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
        user='database',
        passw='batatinha',
        host='localhost',
        port='5432',
        db='livedepystats'
    )


class Production(Base):
    SQLALCHEMY_DATABASE_URI = postgres_uri.format(
        user='database',
        passw='batatinha',
        host='localhost',
        port='5432',
        db='livedepystats'
    )


envs = {
    'base': Base,
    'testing': Testing,
    'development': Development,
    'production': Production
}


def get_env():
    return envs[environ.get('FLASK_ENV', default='production')]
