"""
Django settings for pola project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path

import django
import environ
from boto.s3.connection import OrdinaryCallingFormat
from django.utils.translation import gettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 4  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('pola')

env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    'django.contrib.humanize',
    # Must be before django.contrib.admin
    'dal',
    'dal_select2',
    # Admin
    'grappelli',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'reversion',
    'django_filters',
    'corsheaders',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'pola',
    'pola.gpc',
    'pola.product',
    'pola.company',
    'pola.report',
    'pola.ai_pics',
    'pola.pagination_custom',
    'pola.users',
    'pola.concurency',
    'pola.rpc_api',
    'pola.bi_export',
    'pola.social',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    # 'sites': 'pola.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    # str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Pola Team""", 'pola@pola.pl')]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default="postgres:///pola"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'pl-pl'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

LANGUAGES = (
    ('pl', _('Polish')),
    ('en', _('English')),
)

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [str(APPS_DIR.path('templates'))],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': ['django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader'],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'pola.config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'pola.config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_ADAPTER = 'pola.custom_allauth.NoSignupAccountAdapter'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# Django Filter
FILTERS_DISABLE_HELP_TEXT = True

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {'django.request': {'handlers': ['mail_admins'], 'level': 'ERROR', 'propagate': True}},
}

IS_PRODUCTION = env("IS_PRODUCTION", default=False)

# Your common stuff: Below this line define 3rd party library settings
SLACK_TOKEN = env("SLACK_TOKEN", default=None)
SLACK_CHANNEL_AI_STATS = env("SLACK_CHANNEL_AI_STATS", default=None)

WHITELIST_API_IP_ADDRESS = env.list("WHITELIST_API_IP_ADDRESSES", default=['127.0.0.1'])

AI_PICS_PAGE_SIZE = 5000

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# Uploaded Media Files
# ------------------------
# See: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
INSTALLED_APPS += ('storages',)
if django.VERSION < (4, 0):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STORAGES = {
        "default": {
            "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
        },
        "staticfiles": {
            "BACKEND": 'storages.backends.s3boto3.S3StaticStorage',
        },
    }

AWS_ACCESS_KEY_ID = env('POLA_APP_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('POLA_APP_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('POLA_APP_AWS_S3_PUBLIC_BUCKET_NAME')
AWS_STORAGE_BACKEND_BUCKET_NAME = env('POLA_APP_AWS_S3_BACKEND_BUCKET_NAME')
AWS_STORAGE_AI_PICS_BUCKET_NAME = env('POLA_APP_AWS_S3_AI_PICS_BUCKET_NAME')
AWS_STORAGE_WEB_BUCKET_NAME = env.str('POLA_APP_AWS_S3_WEB_BUCKET_NAME', '')
AWS_STORAGE_COMPANY_LOGOTYPE_BUCKET_NAME = env('POLA_APP_AWS_S3_COMPANY_LOGOTYPE_BUCKET_NAME')
# TODO See: https://github.com/jschneier/django-storages/issues/47
# Revert the following and use str after the above-mentioned bug is fixed in
# either django-storage-redux or boto
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY)}
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = env.bool('DJANGO_AWS_QUERYSTRING_AUTH', False)
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_ENDPOINT_URL = env.str('POLA_APP_AWS_S3_ENDPOINT_URL', default=None)
AI_SHARED_SECRET = env('AI_SHARED_SECRET')

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
if AWS_S3_ENDPOINT_URL:
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/'
else:
    STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR.path('static'))]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
if AWS_S3_ENDPOINT_URL:
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BACKEND_BUCKET_NAME}/'
else:
    MEDIA_URL = f"https://{AWS_STORAGE_BACKEND_BUCKET_NAME}.s3.amazonaws.com/"

# CORS CONFIGURATION
# ------------------------
# For details, see: https://github.com/adamchainz/django-cors-headers
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "https://www.pola-app.pl",
    "https://pola-staging.herokuapp.com",
    "http://kj-pola-app-web-preview.s3-website.eu-central-1.amazonaws.com",
]

CORS_URLS_REGEX = r"^/a/.*$"

# APP CONFIGURATION
# ------------------------

# OPEN API CORE
# ---------------
# https://openapi-core.readthedocs.io/en/latest/integrations/django/#django

from openapi_core import OpenAPI  # noqa: E402

OPENAPI = OpenAPI.from_path(Path(str(ROOT_DIR)) / "pola" / "rpc_api" / "openapi-v1.yaml")

# GET RESPONSE
# ------------------------------------------------------------------------------
GET_RESPONSE = {
    'API_TOKEN': env('POLA_APP_GET_RESPONSE_API_TOKEN'),
    'CAMPAIGN_ID': env('POLA_APP_GET_RESPONSE_CAMPAIGN_ID'),
}

# PRODUKTY W SIECI
# ------------------------------------------------------------------------------
PRODUKTY_W_SIECI_ENABLE = env.bool("POLA_APP_PRODUKTY_W_SIECI_ENABLE", default=True)
PRODUKTY_W_SIECI = {
    'API_TOKEN': env('POLA_APP_PRODUKTY_W_SIECI_API_TOKEN'),
}
