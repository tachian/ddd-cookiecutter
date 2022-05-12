import os
import sys
import logging

import click

import json_logging
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from lutils.api_errors import install_error_handlers
from lutils.services.contract import LendicoContract
from lutils.services.communication import LendicoCommunication


ENV = os.environ.get('DEPLOY_ENV', 'Development')
db = SQLAlchemy()


def create_app(deploy_env: str = ENV) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(f'{{cookiecutter.project_main_folder}}.config.{deploy_env}Config')

    __register_blueprints_and_error_handling(app)
    __configure_logger(app)
    __register_commands(app)
    __configure_lendico_services(app)

    db.init_app(app)

    Migrate(app, db)

    return app


def __register_blueprints_and_error_handling(app: Flask):
    from {{cookiecutter.project_main_folder}}.presentation_layer.views.api import blueprint

    app.register_blueprint(blueprint)

    error_codes = [400, 401, 403, 404, 405, 406, 408, 409, 410, 412,
                   415, 428, 429, 500, 501]
    install_error_handlers(error_codes, app)


def __configure_logger(app: Flask):
    if not json_logging.ENABLE_JSON_LOGGING:
        "Prevent to call json_logging.init_flask() more than once."
        json_logging.ENABLE_JSON_LOGGING = True
        json_logging.init_flask()
        json_logging.init_request_instrument(app)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(app.config["LOGS_LEVEL"])
    app.logger.addHandler(ch)


def __register_commands(app):
    from {{cookiecutter.project_main_folder}}.commands import drop_create_tables

    app.cli.command("drop-create-tables")(drop_create_tables)


def __configure_lendico_services(app: Flask):
    pass