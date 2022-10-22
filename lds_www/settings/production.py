from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['ldswww-production.up.railway.app']
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
CSRF_TRUSTED_ORIGINS = ['https://ldswww-production.up.railway.app']

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CssMinFilter',
]

COMPRESS_CSS_HASING_METHOD = 'content'

DEFAULT_FILE_STORAGE = 'lds_www.settings.storage_backends.MediaStorage'


DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}





try:
    from .local import *
except ImportError:
    pass
