#!/bin/bash

source ~/projects/django_lottopy/django_lottopy/bin/activate
export DJANGO_DEBUG=True
export DJANGO_SECRET_KEY='g_lw__)68m(3x4hq$ehg-(4xyc*@)^na4zd!2io&%x_rovgle$'
redis-server &
#PYTHONPATH=`pwd`/.. gunicorn --bind 0.0.0.0:8000 lottopy_site.wsgi:application

# Debug=True
python ~/projects/django_lottopy/lottopy_site/manage.py runserver
# Debug=False
#gunicorn -c ~/projects/django_lottopy/gunicorn.conf.py lottopy_site.wsgi:application