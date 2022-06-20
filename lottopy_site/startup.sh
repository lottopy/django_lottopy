#!/bin/bash

source ~/django_lottopy/django_lottopy/bin/activate
export DJANGO_DEBUG=False 
export DJANGO_SECRET_KEY='g_lw__)68m(3x4hq$ehg-(4xyc*@)^na4zd!2io&%x_rovgle$'
#redis-server &
#PYTHONPATH=`pwd`/.. gunicorn --bind 0.0.0.0:8000 lottopy_site.wsgi:application

# Debug=True
#python ~/django_lottopy/lottopy_site/manage.py runserver --bind unix:/home/williedynamite/django_lottoy/run/gunicorn.sock
# Debug=False
#gunicorn -c ~/django_lottopy/gunicorn.conf.py --bind 0.0.0.0:8000 lottopy_site.wsgi:application
gunicorn -c ~/django_lottopy/lottopy_site/gunicorn.conf.py --bind unix:/home/williedynamite/django_lottopy/run/gunicorn.sock lottopy_site.wsgi:application


