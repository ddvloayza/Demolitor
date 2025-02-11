# -*- coding: utf-8 -*-
# production.py
import os

from .base import *  # noqa: F403

DEBUG = os.getenv("DEBUG", False)
APPEND_SLASH = True

# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECONDS = 31536000  # 1 año
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True

# DIRS
AWS_ACCESS_KEY_ID = os.environ.setdefault("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_REGION_NAME = os.environ.setdefault("AWS_S3_REGION_NAME", "")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"


STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_LOCATION = "static"

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
MEDIAFILES_LOCATION = "media"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")


# SESSIONS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SMART SELECT
JQUERY_URL = False

# CACHE


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
