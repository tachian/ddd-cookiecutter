import logging
import os

from dotenv import load_dotenv
from env_kills.assertions import EnvKills

load_dotenv()


class BaseConfig(object):
    env_cfg = EnvKills(namespace="{{cookiecutter.env_vars_namespace}}",
                       environment='DEPLOY_ENV')

    DEBUG = False
    TESTING = False
    DEPLOY_ENV = env_cfg.deploy_env(default='Development')
    LOGS_LEVEL = logging.INFO
    RESTPLUS_VALIDATE = True
    SQLALCHEMY_DATABASE_URI = env_cfg.database_uri(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    SQLALCHEMY_DATABASE_URI = BaseConfig.env_cfg.database_uri_test(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}_test")


class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(BaseConfig.env_cfg.log_level(default=logging.INFO))