import logging

from {{cookiecutter.project_main_folder}}.celery_config import celery

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)


example_queue = celery.app.config[
            'QUEUE_EXAMPLE']


@celery.task(
    bind=True,
    name='task.task_example',
    queue=example_queue
)
def task_example(self):
    pass
