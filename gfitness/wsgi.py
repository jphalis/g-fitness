"""
WSGI config for gfitness project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gfitness.settings")

from django.core.wsgi import get_wsgi_application
from django.conf import settings
# from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()

if not settings.DEBUG:
	try:
		from dj_static import Cling
		application = Cling(get_wsgi_application())

	except:
		pass

# application = DjangoWhiteNoise(application)