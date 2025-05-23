#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 4
    done

    echo "PostgreSQL started"
fi

python manage.py makemigartions
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"