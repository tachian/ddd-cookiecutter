import logging
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DEPLOY_ENV = os.environ.get('DEPLOY_ENV', 'Development')
    LOGS_LEVEL = logging.INFO
    RESTPLUS_VALIDATE = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    SQLALCHEMY_DATABASE_URI = "{}_test".format(os.environ.get('DATABASE_URI'))


class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(os.environ.get('LOGS_LEVEL', logging.ERROR))