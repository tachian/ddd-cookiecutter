import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

remove_migrations_dir = {{cookiecutter.database|lower == 'nosql'}}

if remove_migrations_dir:
    remove(os.path.join('{{cookiecutter.project_source}}', 'migrations'))
