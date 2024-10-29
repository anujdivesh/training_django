#!/bin/sh


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi



echo "------------------------------------------------------Hello----------------------------------------------------------------"

python /code/manage.py collectstatic --noinput

# Restore the database if a backup file exists
if [ -f /code/training_db.sql ]; then
  echo "Restoring database from backup..."
  
  # For PostgreSQL
  psql -U postgres -d training-dbms < /code/training30.sql
  
  # For MySQL
  # mysql -u your_username -p your_database < /path/to/backup.sql
  
  echo "Database restored!"
else
  echo "No backup file found. Skipping database restore."
fi

#python /code/manage.py flush --no-input
#python /code/manage.py migrate

#DJANGO_SUPERUSER_PASSWORD=Oceanportal2017* python /code/manage.py createsuperuser --username=admin --email=divesha@spc.int --noinput

#python /code/manage.py runserver 0.0.0.0:8000
exec "$@"