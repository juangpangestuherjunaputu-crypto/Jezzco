#!/bin/sh
set -e
/opt/venv/bin/python manage.py collectstatic --noinput
exec /opt/venv/bin/gunicorn config.wsgi:application --log-file -
