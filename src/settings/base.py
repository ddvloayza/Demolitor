import os
from datetime import timedelta

PROJECT_NAME = "Samiex"
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = bool(int(os.getenv("DEBUG", False)))

ALLOWED_HOSTS = (
    os.getenv("ALLOWED_HOSTS").split(",") if os.getenv("ALLOWED_HOSTS") else []
)

# Application definition
DJANGO_APPS = [
    # solo las aplicaciones propias de django
    "tinymce_4",
    "django.contrib.admin",
    "django.contrib.auth",
    'django.contrib.sites',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ubigeos",

]

LOCAL_APPS = [
    # Aqui van las aplicaciones de  tu local ejem: apps.web
    "apps.customuser",
    "apps.core",
    "apps.product",
    "apps.company",
    "apps.visit",
    "apps.contact",
    "apps.tag",
]


ADMIN_URL = "admin-django"

THIRD_PART_APPS = [
    # Solo aplicaciones externas
    "django_filters",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PART_APPS

CSRF_TRUSTED_ORIGINS = ["https://*.samiex.com.pe", "https://*.127.0.0.1"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.locale.LocaleMiddleware',
]


ROOT_URLCONF = "urls"


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

WSGI_APPLICATION = "wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "NAME": os.getenv("POSTGRES_DB"),
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(levelname)s [%(asctime)s] %(module)s %(message)s"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": os.path.join(BASE_DIR, "django.log"),
            "maxBytes": 1024000,
            "backupCount": 3,
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "propagate": True,
            "level": "DEBUG",
        },
        "django.template.base": {
            "handlers": [],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

# Custom User Model

AUTH_USER_MODEL = "customuser.CustomUser"
USERNAME_REGEX = r"^(?=.{6,30}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9.-]+(?<![_.])$"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# authentication
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # "apps.authentication.backends.TokenAuthenticationBackend",
]


# Internationalization
LANGUAGE_CODE = "es"

TIME_ZONE = "America/Lima"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = os.environ.setdefault("STATIC_URL", "/static/")

# Media files
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = os.environ.setdefault("MEDIA_URL", "/media/")


PAGINATION_SETTINGS = {
    "PAGE_RANGE_DISPLAYED": 10,
    "MARGIN_PAGES_DISPLAYED": 2,
    "SHOW_FIRST_PAGE_WHEN_INVALID": True,
}
LOGIN_URL = "/"

TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "width": 1120,
    "cleanup_on_startup": True,
    "custom_undo_redo_levels": 20,
    "selector": "textarea",
    "theme": "modern",
    "plugins": """
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            """,
    "toolbar1": """
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            """,
    "toolbar2": """
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            """,
    "contextmenu": "formats | link image",
    "menubar": True,
    "statusbar": True,
}

