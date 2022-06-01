{% if cookiecutter.database|lower != 'nosql' -%}
import flask_migrate {%- endif %}
from flask.cli import with_appcontext
from flask import current_app

{% if cookiecutter.database|lower != 'nosql' -%}
from {{cookiecutter.project_main_folder}}.app import db {%- endif %}


class InvalidEnvironment(Exception):
    pass


{% if cookiecutter.database|lower != 'nosql' -%}
def _drop_tables():
    with db.get_engine().begin() as conn:
        {% if cookiecutter.database|lower == 'postgres' -%}
        result = conn.execute("SELECT tablename FROM pg_tables WHERE schemaname = current_schema();")
        {%- elif cookiecutter.database|lower == 'mysql' -%}
        result = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = database();") {%- endif %}
        for row in result:
            conn.execute(f'drop table {row[0]} CASCADE;')

def _drop_create_tables():
    _drop_tables()
    db.session.commit()
    flask_migrate.upgrade()
    db.session.commit() {%- endif %}

@with_appcontext
def drop_create_tables():
    if current_app.config["DEPLOY_ENV"] == 'Production':
        raise InvalidEnvironment('Drop/Create tables unable for production')
    {% if cookiecutter.database|lower != 'nosql' -%}
    _drop_create_tables()
    {% else -%}
    print("Not implemented") {%- endif %}
