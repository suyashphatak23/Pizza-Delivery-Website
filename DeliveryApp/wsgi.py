"""
WSGI config for DeliveryApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from django.conf.settings import BASE_DIR, STATIC_ROOT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeliveryApp.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
application.add_files(os.path.join(BASE_DIR, 'static'), prefix="more-files/")