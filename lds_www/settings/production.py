from .base import *
import os

# Todo move to env
DEBUG = False
ALLOWED_HOSTS = ['ldswww-production.up.railway.app', 'www.lunadentalstudio.com', 'lunadentalstudio.com',]
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
CSRF_TRUSTED_ORIGINS = ['https://ldswww-production.up.railway.app', 'https://lunadentalstudio.com', 'https://www.lunadentalstudio.com']

DEFAULT_FILE_STORAGE = 'lds_www.settings.storage_backends.MediaStorage'




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
