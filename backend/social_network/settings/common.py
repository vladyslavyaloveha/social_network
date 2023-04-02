"""Django settings for social_network project.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import logging.config
import os
from datetime import timedelta
from pathlib import Path

import environ
import structlog

env = environ.Env()

# Build paths inside the project.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/4.0/ref/settings/#debug
DEBUG = env.bool("DEBUG", default=False)

# https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# https://docs.djangoproject.com/en/4.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "social_network.wsgi.application"

# https://docs.djangoproject.com/en/4.0/ref/settings/#root-urlconf
ROOT_URLCONF = "social_network.urls"

# https://docs.djangoproject.com/en/4.0/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

# Application definition
# https://docs.djangoproject.com/en/4.0/ref/applications/
INSTALLED_APPS = [
    # Admin theme
    # https://github.com/fabiocaccamo/django-admin-interface
    "admin_interface",
    # Standard library applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party applications
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "colorfield",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "rest_framework.authtoken",
    "dj_rest_auth.registration",
    # Project applications
    "social_network.apps.users",
    "social_network.apps.posts",
    "social_network.apps.activity",
]

# Middleware
# https://docs.djangoproject.com/en/4.0/topics/http/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_structlog.middlewares.RequestMiddleware",
    # custom middlewares
    "social_network.apps.activity.middlewares.LastActiveMiddleware",
]

# Templates
# https://docs.djangoproject.com/en/4.0/topics/templates/
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases/
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env.str("DB_HOST"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "PORT": env.int("DB_PORT", default=5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators/
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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

# All-auth configuration
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = "none"

# JWT Settings
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "UPDATE_LAST_LOGIN": True,
}

# https://docs.djangoproject.com/en/4.0/ref/settings/#time-zone
TIME_ZONE = "UTC"

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# Django REST Framework Spectacular
# https://drf-spectacular.readthedocs.io/en/latest/
SPECTACULAR_SETTINGS = {
    "TITLE": "Social Network",
    "VERSION": "1.0.0",
    "CONTACT": {"email": "vladyslavyaloveha@gmail.com"},
    "TAGS": [
        {
            "name": "posts",
            "description": "Manage posts",
        },
        {
            "name": "analytics",
            "description": "Calculate analytics",
        },
        {
            "name": "activity",
            "description": "Activity statistics",
        },
    ],
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# Logging
# https://docs.djangoproject.com/en/4.0/topics/logging/
LOG_FILE = env.str("LOG_FILE")
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
        },
        "json_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_FILE,
            "formatter": "json_formatter",
            "when": "W6",  # Sunday
        },
    },
    "loggers": {
        "": {"handlers": ["console", "json_file"], "level": "INFO", "propagate": False},
        "logger": {
            "handlers": ["console", "json_file"],
            "level": "DEBUG" if DEBUG else "INFO",
            "propagate": False,
        },
    },
}

# Structured logging
# https://www.structlog.org/en/stable/
# https://django-structlog.readthedocs.io/en/latest/
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.CallsiteParameterAdder(
            [
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.LINENO,
            ],
        ),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
logging.config.dictConfig(LOGGING)

# https://docs.djangoproject.com/en/4.0/ref/settings/#silenced-system-checks
SILENCED_SYSTEM_CHECKS = ["security.W019"]
