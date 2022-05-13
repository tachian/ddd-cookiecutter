from flask.cli import with_appcontext
from {{cookiecutter.project_main_folder}}.app import db


@with_appcontext
def drop_create_tables():
    db.session.commit()
    db.drop_all()
    db.create_all()
    db.session.commit()
