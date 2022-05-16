import logging
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from {{cookiecutter.project_main_folder}}.app import create_app


app = create_app()

scheduler = BlockingScheduler(timezone='America/Sao_Paulo')

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)


@scheduler.scheduled_job(trigger='cron', minute='*')
def example_scheduled_job():
    pass


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    except Exception as e:
        logger.exception(e.message)