#!/bin/sh

echo "Generate migrations"
python /www/src/manage.py makemigrations

echo "Apply database migrations"
python /www/src/manage.py migrate

echo "Starting server"
python /www/src/manage.py runserver 0.0.0.0:8000
