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

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles" # collectstatic -- not needed? only if you have multiple static files (one in each app) and want to collect them into one static folder to make it easier to serve in a production environment

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "{{ cookiecutter.project_name }}" / "static",
]

# Media files uploaded by users
MEDIA_ROOT = BASE_DIR / "{{ cookiecutter.project_name }}" / "media"

MEDIA_URL = '/media/'




