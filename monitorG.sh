#!/bin/bash

PLIST="gunicorn redis nginx"

for p in $PLIST 
do
	pgrep $p
	if [ $? -ne 0 ]
	then 	
	/etc/init.d/$p start >/dev/null	
fi
done
#gunicorn -c /home/williedynamite/django_lottopy/gunicorn.conf.py --workers 3 --bind unix:/root/django_lottopy/django_lottopy.sock lottopy_site.wsgi:application
