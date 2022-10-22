from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS')

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CssMinFilter',
]

COMPRESS_CSS_HASING_METHOD = 'content'


MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass
