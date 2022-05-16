#!/usr/bin/env bash

set -ef

cli_help() {
  cli_name=${0##*/}
  echo "
$cli_name
CDC-MANAGER entrypoint cli
Usage: $cli_name [command] [queues]
Commands:
  {% if cookiecutter.create_celery_tasks == 'y' -%}
  worker    deploy worker {%- endif %}
  {% if cookiecutter.create_clock == 'y' -%}
  clock     deploy clock {%- endif %}
  web       deploy web
  migrate   deploy migrate
  *         Help
"
  exit 1
}

case "$1" in
  {% if cookiecutter.create_celery_tasks == 'y' -%}
  worker)
    newrelic-admin run-program celery -A {{cookiecutter.project_main_folder}}.app:celery_app worker -Q "$2" --loglevel INFO --concurrency=1 -E
    ;; {%- endif %}
  {% if cookiecutter.create_clock == 'y' -%}
  clock)
    newrelic-admin run-program python scheduler.py
    ;; {%- endif %}
  web)
    uwsgi --ini ./uwsgi.ini --enable-threads --single-interpreter --gevent 100
    ;;
  migrate)
    flask db upgrade
    ;;
  *)
    cli_help
    ;;
esac