from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ldswww-production.up.railway.app']

try:
    from .local import *
except ImportError:
    pass
