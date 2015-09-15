import os
from django.conf import settings


#heroku run bash
#this gives you the heroku terminal so you can run all stuff like:
#$ python manage.py collecstatic


if not settings.DEBUG:

    # INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'carts',
    # 'contact',
    # 'crispy_forms',
    # 'localflavor',
    # 'marketing',
    # 'orders',
    # 'products',
    # 'profiles',
    # 'schedule',
    # )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        }
    }

    try:
        # Heroku database
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()
    except:
        pass

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['*']

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

#     MEDIA_URL = '/media/'

#     MEDIA_ROOT = os.path.join(os.path.dirname(settings.BASE_DIR), "src", "static", "media")

    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    MEDIAFILES_DIRS = (
        os.path.join(BASE_DIR, 'static', 'media')
    )

    # MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
