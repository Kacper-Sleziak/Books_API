#! /bin/sh

python3 /django/manage.py wait_for_db
python3 /django/manage.py makemigrations
python3 /django/manage.py migrate
python3 /django/manage.py runserver 0.0.0.0:8000 --insecure
