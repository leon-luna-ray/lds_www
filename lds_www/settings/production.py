from .base import *
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['ldswww-production.up.railway.app']
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
CSRF_TRUSTED_ORIGINS = ['https://ldswww-production.up.railway.app']

DEFAULT_FILE_STORAGE = 'lds_www.settings.storage_backends.MediaStorage'


DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_QUERY_STRING_AUTH = False
AWS_LOCATION = 'static'
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN



try:
    from .local import *
except ImportError:
    pass
