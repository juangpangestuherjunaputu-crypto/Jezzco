web: /opt/venv/bin/python manage.py collectstatic --noinput && /opt/venv/bin/gunicorn config.wsgi:application --log-file -
release: python manage.py migrate --noinput