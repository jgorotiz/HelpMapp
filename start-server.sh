#!/usr/bin/env bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd helpmapp || exit 127;python manage.py createsuperuser --no-input)
fi
(cd helpmapp;python manage.py migrate)
(cd helpmapp;python manage.py loaddata sample_data/*.json)
(cd helpmapp; gunicorn daw.wsgi --user www-data --bind 0.0.0.0:8010 &)
nginx -g 'daemon off;'