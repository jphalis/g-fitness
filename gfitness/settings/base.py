import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0xd@ioxu5e4e=z+%ovyz$qyu&d0qy0ai5)-k%@)r7%qztgybbe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

SITE_URL = "*"

ADMINS = (
    ('JP', 'jphalisnj@gmail.com'),
)

# ========================== EMAIL SETTINGS =======================
DEFAULT_FROM_EMAIL = "G Fitness <bryongarcia73@yahoo.com>"

EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_HOST_USER = 'bryongarcia73@yahoo.com'
EMAIL_HOST_PASSWORD = 'Katiehotass69'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ========================== APPLICATIONS ==========================

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # 'carts',
    'contact',
    'crispy_forms',
    'localflavor',
    'marketing',
    # 'orders',
    # 'products',
    'profiles',
    'schedule',
)

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# ========================== USER AUTHENTICATION SETTINGS ==========================

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"  # (="username" | "email" | "username_email")
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None  # choices are: "mandatory", "optional", or None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"  # if secure use https
ACCOUNT_LOGOUT_ON_GET = True  # log user out right away.
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_SIGNUP_FORM_CLASS = None  # add a custom sign up form
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True  # use False if you don't want double password fields
ACCOUNT_UNIQUE_EMAIL = True  # enforces emails are unique to all accounts
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"  # If you're using a Custom Model, maybe it's "email"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
# ACCOUNT_USER_DISPLAY (=a callable returning user.username)
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_BLACKLIST = ['some_username_youdon\'t_want']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False  # don't show the password
ACCOUNT_PASSWORD_MIN_LENGTH = 4  # min length of password
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True  # login the user after confirming email, if required.

# ========================== STRIPE SETTINGS ==========================

# Test Keys
STRIPE_SECRET_KEY = 'sk_test_pDgXLZstTUGg8jRBCQQuZYCZ'
STRIPE_PUBLISHABLE_KEY = 'pk_test_dFaYmsKlzHHtUdQjgDVLoCJ9'

# Live Keys
# STRIPE_SECRET_KEY = 'sk_live_N1xdi3O50CczQoFlg2tmiuLB'
# STRIPE_PUBLISHABLE_KEY = 'pk_live_pblLnXiDokzeWT96XOesf2AS'

DEFAULT_TAX_RATE = 0.08  # 8%

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

#     MEDIA_URL = '/media/'

#     STATIC_URL = '/static/'

#     MEDIA_ROOT = os.path.join(os.path.dirname(settings.BASE_DIR), "src", "static", "media")

#     STATIC_ROOT = os.path.join(os.path.dirname(settings.BASE_DIR), "src", "static", "root")

#     STATICFILES_DIRS = (
#         os.path.join(os.path.dirname(settings.BASE_DIR), "src", "static", "static"),
#     )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

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
