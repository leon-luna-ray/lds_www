from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ldswww-production.up.railway.app']
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CssMinFilter',
]

COMPRESS_CSS_HASING_METHOD = 'content'

try:
    from .local import *
except ImportError:
    pass
