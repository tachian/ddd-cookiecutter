import logging
import os

from dotenv import load_dotenv
from env_kills.assertions import EnvKills
import json

load_dotenv()


class BaseConfig(object):
    env_cfg = EnvKills(namespace="{{cookiecutter.env_vars_namespace}}",
                       environment='DEPLOY_ENV')

    DEBUG = False
    TESTING = False
    DEPLOY_ENV = env_cfg.deploy_env(default='Development')
    LOGS_LEVEL = logging.INFO
    RESTPLUS_VALIDATE = True
    {% if cookiecutter.database|lower == 'mysql' -%}
    SQLALCHEMY_DATABASE_URI = env_cfg.database_uri(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    {% elif cookiecutter.database|lower == 'postgres' -%}
    SQLALCHEMY_DATABASE_URI = env_cfg.database_uri(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    SQLALCHEMY_TRACK_MODIFICATIONS = True {%- endif %}

    {% if cookiecutter.create_celery_tasks == 'y' -%}
    # Celery
    BROKER_URL = env_cfg.broker_url(default='sqs://')
    BROKER_TRANSPORT_OPTIONS = json.loads(
        env_cfg.broker_transport_options(default='{}'))
    QUEUE_EXAMPLE = env_cfg.queue_example(default='queue_example') {%- endif %}


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    {% if cookiecutter.database|lower == 'mysql' -%}
    SQLALCHEMY_DATABASE_URI = BaseConfig.env_cfg.database_uri_test(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    {%- elif cookiecutter.database|lower == 'postgres' -%}
    SQLALCHEMY_DATABASE_URI = BaseConfig.env_cfg.database_uri_test(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}_test") {%- endif %}


class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(BaseConfig.env_cfg.log_level(default=logging.INFO))
