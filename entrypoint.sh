#!/bin/bash

python manage.py migrate &&
python manage.py insert_data &&
python manage.py createsuperuser --noinput || true &&
gunicorn lit3d.wsgi:application --bind 0.0.0.0:8000