from .base import *

DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0:$PORT']

try:
    from .local import *
except ImportError:
    pass
