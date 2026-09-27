#!/bin/bash

source /home/williedynamite/django_lottopy/django_lottopy/bin/activate
export DJANGO_DEBUG=False
source /home/williedynamite/django_lottopy/.env
#export TMPDIR='/home/williedynamite/django_lottopy/tmp'
gunicorn -c /home/williedynamite/django_lottopy/lottopy_site/gunicorn.conf.py --bind unix:/home/williedynamite/django_lottopy/run/gunicorn.sock --log-level debug --timeout 600 lottopy_site.wsgi:application --reload

#redis-server &
#PYTHONPATH=`pwd`/.. gunicorn --bind 0.0.0.0:8000 lottopy_site.wsgi:applicationDebug=True
#python ~/django_lottopy/lottopy_site/manage.py runserver --bind unix:/home/williedynamite/django_lottoy/run/gunicorn.sock
# Debug=False
#gunicorn -c ~/django_lottopy/lottopy_site/gunicorn.conf.py --bind 0.0.0.0:8000 --access-logfile '-' --error-logfile '-' --log-level debug --timeout 600 lottopy_site.wsgi:application --reload


