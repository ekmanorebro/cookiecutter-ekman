import os
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
APPS_DIR = BASE_DIR / 'django_ekman' / 'apps'

SECRET_KEY = config('SECRET_KEY')

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    'django_ekman.apps.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_ekman.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_ekman.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTHENTICATION

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:detail'
LOGIN_URL = 'users:login'




## TO DO:
## the static files url, media, etc..
## custom user model...
## turn it into cookiecutter template
## see what WSGI_APPLICATION is
## see if you need to add anything else..
## .gitignore => .env
## see if you need to divide the base, local, production any further, or if it's done
## see what you have to do with the database..
## see if it works, with a new app, with template, and urls, static files, and all of that..



