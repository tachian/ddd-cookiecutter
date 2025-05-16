import os
import sys
import logging
import click

import json_logging
from flask import Flask
from flask_cors import CORS
{% if cookiecutter.database|lower != 'nosql' -%}
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate {%- endif %}
from main.presentation_layer import install_error_handlers
{% if cookiecutter.database|lower != 'nosql' -%}
from sqlalchemy import MetaData {%- endif %}

{% if cookiecutter.create_celery_tasks == 'y' -%}
from {{cookiecutter.project_main_folder}}.celery_config import celery {%- endif %}


ENV = os.environ.get('DEPLOY_ENV', 'Development')

{% if cookiecutter.database|lower != 'nosql' -%}
convention = {
    "ix": "ix_%(column_0_label)s",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
    "uq": "%(table_name)s_%(column_0_name)s_key"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata) {%- endif %}


def create_app(deploy_env: str = ENV) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(f'{{cookiecutter.project_main_folder}}.config.{deploy_env}Config')

    __register_blueprints_and_error_handling(app)
    __configure_logger(app)
    __register_commands(app)

    {% if cookiecutter.database|lower != 'nosql' -%}
    db.init_app(app)
    Migrate(app, db) {%- endif%}

    {% if cookiecutter.create_celery_tasks == 'y' -%}
    celery.init_app(app) {%- endif %}

    return app

def __register_blueprints_and_error_handling(app: Flask):
    from {{cookiecutter.project_main_folder}}.presentation_layer.views.api import blueprint

    app.register_blueprint(blueprint)

    error_codes = [400, 401, 403, 404, 405, 406, 408, 409, 410, 412,
                   415, 428, 429, 500, 501]
    install_error_handlers(error_codes, app)


def __configure_logger(app: Flask):
    if not json_logging.ENABLE_JSON_LOGGING:
        json_logging.init_flask(enable_json=True)
        json_logging.init_request_instrument(app)

    logger = logging.getLogger("{{cookiecutter.project_slug}}")
    logger.setLevel(app.config["LOGS_LEVEL"])
    logger.addHandler(logging.StreamHandler(sys.stdout))


def __register_commands(app):
    from {{cookiecutter.project_main_folder}}.commands import drop_create_tables

    app.cli.command("drop-create-tables")(drop_create_tables)


{% if cookiecutter.create_celery_tasks == 'y' -%}
def create_celery_app():
    create_app()
    return celery

celery_app = create_celery_app() {%- endif %}
