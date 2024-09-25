# -*- coding: utf-8 -*-
# production.py
import os

from .base import *  # noqa: F403

DEBUG = os.getenv("DEBUG", False)
PREPEND_WWW = False


# DIRS

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = os.environ.setdefault("MEDIA_URL", "/media/")
ALLOWED_HOSTS = ["*"]
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = os.environ.setdefault("STATIC_URL", "/static/")



SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SMART SELECT
JQUERY_URL = False

# CACHE
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
        "TIMEOUT": "300",
    }
}


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(BASE_DIR), "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.views.webpage_processor",
            ],
        },
    },
]

# RAVEN_CONFIG = {
#     'dsn': 'https://bc53ee614b2a42bda1c6eff9127e17ca:3ee315a5d30e4d7aad1b8c2cfb893897@sentry.io/1273222',
# }
