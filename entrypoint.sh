#!/bin/sh


echo "------------------------------------------------------Hello----------------------------------------------------------------"

python /code/manage.py collectstatic --noinput
#python /code/manage.py flush --no-input
#python /code/manage.py migrate

#DJANGO_SUPERUSER_PASSWORD=Oceanportal2017* python /code/manage.py createsuperuser --username=admin --email=divesha@spc.int --noinput

#python /code/manage.py runserver 0.0.0.0:8000
exec "$@"