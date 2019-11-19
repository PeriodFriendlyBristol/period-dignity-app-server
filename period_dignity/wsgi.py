"""
WSGI config for period_dignity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'period_dignity.settings')

application = get_wsgi_application()
