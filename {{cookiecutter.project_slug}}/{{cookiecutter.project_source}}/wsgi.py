{% if cookiecutter.database|lower != 'nosql' -%}
from {{cookiecutter.project_main_folder}}.app import create_app, db
{% else -%}
from {{cookiecutter.project_main_folder}}.app import create_app
{%- endif %}

app = create_app()
{% if cookiecutter.database|lower != 'nosql' -%}
with app.app_context():
    db.metadata.bind = db.engine
{%- endif %}

