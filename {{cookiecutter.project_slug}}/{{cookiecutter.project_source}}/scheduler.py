import logging
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from {{cookiecutter.project_main_folder}}.app import create_app


app = create_app()

scheduler = BlockingScheduler(timezone='America/Sao_Paulo')

aps_logger = logging.getLogger('apscheduler.executors.default')
aps_logger.setLevel(app.config['LOGS_LEVEL'])
aps_logger.addHandler(logging.StreamHandler(sys.stdout))
logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)


@scheduler.scheduled_job(trigger='cron', minute='*')
def example_scheduled_job():
    with app.app_context():
        logger.info("Example job executed")


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    except Exception as e:
        logger.exception(e.message)
