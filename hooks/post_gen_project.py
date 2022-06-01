import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

remove_migrations_dir = {{cookiecutter.database|lower == 'nosql'}}
remove_scheduler_file = {{cookiecutter.create_clock == 'n'}}
remove_celery_files = {{cookiecutter.create_celery_tasks == 'n'}}

if remove_migrations_dir:
    remove(os.path.join('{{cookiecutter.project_source}}', 'migrations', 'alembic.ini'))
    remove(os.path.join('{{cookiecutter.project_source}}', 'migrations', 'env.py'))
    remove(os.path.join('{{cookiecutter.project_source}}', 'migrations', 'script.py.mako'))

if remove_scheduler_file:
    remove(os.path.join('{{cookiecutter.project_source}}', 'scheduler.py')),

if remove_celery_files:
    remove(os.path.join('{{cookiecutter.project_source}}',
                        '{{cookiecutter.project_main_folder}}',
                        'celery_config.py'))
    remove(os.path.join('{{cookiecutter.project_source}}',
                        '{{cookiecutter.project_main_folder}}',
                        'application_layer',
                        'tasks.py'))
