# /instance/config.py

# source env/bin/activate
# export FLASK_APP="run.py"
# export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
# export APP_SETTINGS="development"
# export DATABASE_URL="postgresql://localhost/flask_api"
# $ echo "source `which activate.sh`" >> ~/.bashrc
# $ source ~/.bashrc

import os


class DatabaseConfig:
    host = None
    port = None
    name = None
    password = None

    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password

    def get_uri(self):
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}?sslmode=require"


class Config(object):
    """Parent configuration class."""
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SECRET_KEY = "some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
    APP_SETTINGS = "development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY ='jwt-secret-string'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = DatabaseConfig(
        "ec2-23-23-216-40.compute-1.amazonaws.com",
        "5432",
        "d80922ahko5137",
        "phghhujuxxkvsw",
        "44bbd319299761082424509b7a7cae31a36c5f34225d64498046735970c8b914"
    ).get_uri()


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True

    SQLALCHEMY_DATABASE_URI = DatabaseConfig(
        "ec2-107-21-126-193.compute-1.amazonaws.com",
        "5432",
        "dere685c30rvii",
        "xldxtyaysypcac",
        "e73b8c710b58aab41f2d43eb8e4f9e274026ba83dfb51fcc9c62e008fc72d963"
    ).get_uri()

    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
