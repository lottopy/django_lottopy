"""
WSGI config for lottopy_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE']='lottopy_site.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lottopy_site.settings')
application = get_wsgi_application()

virtualenv = "/home/williedynamite/projects/django_lottopy/django_lottopy/bin/activate"