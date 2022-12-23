from .settings import *

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = BASE_DIR.parent

env = environ.Env()
env.read_env(BASE_DIR / ".env")


DEBUG = env.bool("DEBUG")
SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    "core",
    "user",
]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


STATIC_ROOT = "static_root"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media Files
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Custom user
AUTH_USER_MODEL = "user.User"
