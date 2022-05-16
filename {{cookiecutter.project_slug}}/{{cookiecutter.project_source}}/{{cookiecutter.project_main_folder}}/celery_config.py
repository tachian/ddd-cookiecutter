import flask
from celery import Celery
from kombu import Queue, Exchange


class FlaskCelery(Celery):

    def __init__(self, *args, **kwargs):

        super(FlaskCelery, self).__init__(*args, **kwargs)
        self.patch_task()
        self.app = None

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
                else:
                    with _celery.app.app_context():
                        return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app
        self._configure_backend()
        self.autodiscover_tasks(packages={"{{cookiecutter.project_main_folder}}.application_layer.tasks"})

    def _configure_backend(self):
        if not self.app:
            raise Exception("Must call init_app first")

        example_queue = self.app.config[
            'QUEUE_EXAMPLE']

        TASK_QUEUES = (
            Queue(example_queue,
                  Exchange(example_queue),
                  routing_key=example_queue),
        )

        confs = {
            'broker_url': self.app.config['BROKER_URL'],
            'task_queues': TASK_QUEUES,
            'broker_transport_options': self.app.config['BROKER_TRANSPORT_OPTIONS']
        }

        self.conf.update(**confs)


celery = FlaskCelery()
