from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CSS, JavaScript, Images
STATIC_ROOT = BASE_DIR / "{{ cookiecutter.project_name }}" / "apps" / "static"
STATIC_URL = '/static/'

# Media files uploaded by users
MEDIA_ROOT = BASE_DIR / "{{ cookiecutter.project_name }}" / "apps" / "media"
MEDIA_URL = '/media/'





