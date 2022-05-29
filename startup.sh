#!/bin/bash

source ~/projects/django_lottopy/bin/activate
redis-server &
python ~/projects/django_lottopy/lottopy_site/manage.py runserver