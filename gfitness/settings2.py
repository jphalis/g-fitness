"""
Django settings for gfitness project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0xd@ioxu5e4e=z+%ovyz$qyu&d0qy0ai5)-k%@)r7%qztgybbe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

SITE_URL = "www.gfitness.co/"

# ========================== EMAIL SETTINGS =======================
DEFAULT_FROM_EMAIL = "G Fitness <example@gmail.com>"

# try:
#     from .email_settings import host, user, password
EMAIL_HOST = 'smtp.gmail.com' #host
EMAIL_HOST_USER = 'example@gmail.com' #user
EMAIL_HOST_PASSWORD = 'example' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# except:
#     pass

# ========================== ADMIN INTERFACE SETTINGS ==========================

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': "G Fitness",
    'HEADER_DATE_FORMAT': 'D, F j, Y',
    'HEADER_TIME_FORMAT': 'h:i:s A T',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'auth', 'label': 'Users', 'icon': 'icon-lock',\
            'models': ('user', 'group')},
        {'app': 'profiles', 'label': 'User Information', 'icon': 'icon-user',\
            'models': ('userstripe', 'useraddress', 'userdefaultaddress', 'emailmarketingsignup', 'lessoncount')},
        {'app': 'account', 'label': 'Email Addresses', 'icon': 'icon-envelope',\
            'models': ('emailaddress', 'emailconfirmation')},
        {'app': 'schedule', 'label': 'Schedule', 'icon': 'icon-shopping-cart',\
            'models': ('calendar', 'event', 'calendarrelation', 'rule')},
        {'app': 'marketing', 'label': 'Marketing', 'icon': 'icon-globe',\
            'models': ('marketingmessage', 'slider', 'media')},
        {'app': 'products', 'label': 'Products', 'icon': 'icon-tags',\
            'models': ('product', 'productimage', 'variation', 'category')},
        {'app': 'carts', 'label': 'Carts', 'icon': 'icon-shopping-cart',\
            'models': ('cart', 'cartitem')},
        {'app': 'orders', 'label': 'Orders', 'icon': 'icon-th-list',\
            'model': ('order')},
        {'label': 'Settings', 'icon': 'icon-cog',\
            'models': ('auth.user', 'auth.group')},
    ),

    # misc
    'LIST_PER_PAGE': 18
}

# ========================== APPLICATIONS ==========================

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'carts',
    'contact',
    'crispy_forms',
    'localflavor',
    'marketing',
    'orders',
    'products',
    'profiles',
    'schedule',
)

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# ========================== USER AUTHENTICATION SETTINGS ==========================

LOGIN_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email" #(="username" | "email" | "username_email")
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =  LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_EMAIL_VERIFICATION = None #choices are: "mandatory", "optional", or None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" #if secure use https
ACCOUNT_LOGOUT_ON_GET = True #log user out right away.
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_SIGNUP_FORM_CLASS = None # add a custom sign up form
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True # use False if you don't want double password fields
ACCOUNT_UNIQUE_EMAIL = True #enforces emails are unique to all accounts
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username" # If you're using a Custom Model, maybe it's "email"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email" 
# ACCOUNT_USER_DISPLAY (=a callable returning user.username)
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_BLACKLIST = ['some_username_youdon\'t_want']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False #don't show the password
ACCOUNT_PASSWORD_MIN_LENGTH = 4 #min length of password
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True #login the user after confirming email, if required.

# ========================== STRIPE SETTINGS ==========================

# Test Keys
STRIPE_SECRET_KEY = 'sk_test_pDgXLZstTUGg8jRBCQQuZYCZ'
STRIPE_PUBLISHABLE_KEY = 'pk_test_dFaYmsKlzHHtUdQjgDVLoCJ9'

# Live Keys
# STRIPE_SECRET_KEY = 'sk_live_N1xdi3O50CczQoFlg2tmiuLB'
# STRIPE_PUBLISHABLE_KEY = 'pk_live_pblLnXiDokzeWT96XOesf2AS'

DEFAULT_TAX_RATE = 0.08 # 8%

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',
)

ROOT_URLCONF = 'gfitness.urls'

WSGI_APPLICATION = 'gfitness.wsgi.application'


# ========================== DATABASE SETTINGS ==========================
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '[YOUR_DATABASE_NAME]',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }

}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MARKETING_HOURS_OFFSET = 3
MARKETING_SECONDS_OFFSET = 0

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.csrf",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# ========================== FILE SETTINGS ==========================

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "src", "static", "media")

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "src", "static", "root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "src", "static", "static"),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "src", "templates"),
)


if not DEBUG:
    try:
        #Heroku database
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()
    except:
        pass

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['*']




