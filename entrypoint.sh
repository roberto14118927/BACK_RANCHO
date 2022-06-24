#!/bin/sh

python manage.py migrate

python manage runserver 0.0.0.0:8000
