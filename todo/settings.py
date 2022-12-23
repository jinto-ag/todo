from pathlib import Path

from .config.base import *

DEBUG = env.bool("DEBUG")

if DEBUG:
    from .config.development import *
else:
    from .config.production import *
