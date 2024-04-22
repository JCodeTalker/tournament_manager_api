"""
Django settings for project tour_man.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os

from corsheaders.defaults import default_headers, default_methods
from smart_getenv import getenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-ltijngl1u0^!*&x$s5loa%s6r3fgvcj9cr$vq9+g01hi*6)#o4')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', type=bool, default=True)

# ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', type=list, default=['*'])
ALLOWED_HOSTS = ['*']

# If the app is running behind a proxy, this variable must be set with the proxy path
# See https://docs.djangoproject.com/en/5.0/ref/settings/#force-script-name

FORCE_SCRIPT_NAME = os.getenv('PROXY_SCRIPT_NAME', None)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'drf_yasg',
    'rest_framework',
    'apps.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.application_info',
            ]
        },
    }
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES_ENGINE_MAP = {
    'mysql': 'django.db.backends.mysql',
    'oracle': 'django.db.backends.oracle',
    'postgresql': 'django.db.backends.postgresql',
    'postgresql_psycopg2': 'django.db.backends.postgresql_pycopg2',
    'sqlite3': 'django.db.backends.sqlite3',
}

DATABASES = {
    'default': {
        'ENGINE': DATABASES_ENGINE_MAP.get(os.getenv('DB_ENGINE', 'sqlite3')),
        'NAME': os.getenv('DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'CONN_MAX_AGE': getenv('DB_CONN_MAX_AGE', type=int, default=0),
    }
}

if os.environ.get('DB_ENGINE') == 'oracle':
    DATABASES['default']['OPTIONS'] = {'threaded': True, 'use_returning_into': False}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_PATH = os.getenv('STATIC_PATH', '/static/')
STATIC_URL = os.getenv(
    'STATIC_URL',
    (FORCE_SCRIPT_NAME + STATIC_PATH if FORCE_SCRIPT_NAME else STATIC_PATH),
)
STATIC_ROOT = os.getenv('STATIC_ROOT')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# django-cors-headers
# https://pypi.org/project/django-cors-headers/

CORS_ORIGIN_ALLOW_ALL = getenv('CORS_ORIGIN_ALLOW_ALL', type=bool, default=True)
CORS_ORIGIN_WHITELIST = getenv('CORS_ORIGIN_WHITELIST', type=list, default=[])
CORS_ORIGIN_REGEX_WHITELIST = [
    '%r' % value
    for value in getenv('CORS_ORIGIN_REGEX_WHITELIST', type=list, default=[])
]
CORS_ALLOW_HEADERS = getenv(
    'CORS_ALLOW_HEADERS', type=list, default=list(default_headers)
)
CORS_ALLOW_METHODS = getenv(
    'CORS_ALLOW_METHODS', type=list, default=list(default_methods)
)

# Django REST framework
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}


# Application definitions

APP_VERSION = '1.0.0'
APP_NAME = 'tour_man'
APP_DESCRIPTION = 'A RESTfull API for project tour_man'
