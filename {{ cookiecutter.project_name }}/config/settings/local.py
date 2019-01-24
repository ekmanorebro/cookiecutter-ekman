from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles" # collectstatic

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "{{ cookiecutter.project_name }}" / "static",
]

# Media files uploaded by users
MEDIA_ROOT = BASE_DIR / "{{ cookiecutter.project_name }}" / "media"

MEDIA_URL = '/media/'