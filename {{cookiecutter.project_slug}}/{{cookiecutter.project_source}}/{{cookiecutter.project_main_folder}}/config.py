import logging
import os

from dotenv import load_dotenv

import json

load_dotenv()


class BaseConfig(object):

    DEBUG = False
    TESTING = False
    DEPLOY_ENV = os.environ.get('DEPLOY_ENV', 'Development')
    LOGS_LEVEL = logging.INFO
    RESTPLUS_VALIDATE = True
    {% if cookiecutter.database|lower == 'mysql' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', "mysql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    {% elif cookiecutter.database|lower == 'postgres' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', "postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    {% elif cookiecutter.database|lower == 'sqlite' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', 'sqlite:///:memory:')
    SQLALCHEMY_TRACK_MODIFICATIONS = True {%- endif %}

    {% if cookiecutter.create_celery_tasks == 'y' -%}
    # Celery
    BROKER_URL = os.environ.get('BROKER_URL', 'sqs://')
    BROKER_TRANSPORT_OPTIONS = json.loads(
        os.environ.get('BROKER_TRANSPORT_OPTIONS', '{}'))
    QUEUE_EXAMPLE = os.environ.get('QUEUE_EXAMPLE', 'queue_example') 
    {%- endif %}


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    {% if cookiecutter.database|lower == 'mysql' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get(default="mysql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}")
    {%- elif cookiecutter.database|lower == 'postgres' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get(default="postgresql://runner:@localhost:5432/{{cookiecutter.project_slug.replace('-', '_')}}_test")
    {% elif cookiecutter.database|lower == 'sqlite' -%}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', 'sqlite:///:memory:')
    {%- endif %}
class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(os.environ.get('LOG_LEVEL', default=logging.INFO))
