from myproject.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = 'myproject_staging'

INSTALLED_APPS += (
    'gunicorn',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_SUBJECT_PREFIX = '[Myproject Staging] '

COMPRESS_ENABLED = True
