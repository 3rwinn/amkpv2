# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\amkp\wsgi.py
# Size of source mod 2**32: 401 bytes
# Decompiled by https://python-decompiler.com
"""
WSGI config for amkp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amkp.settings')
application = get_wsgi_application()
