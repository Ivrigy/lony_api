from pathlib import Path
import environ
import dj_database_url
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    DEV=(bool, False),
)
if (env_file := BASE_DIR / ".env").exists():
    env.read_env(env_file)

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
DEV = env("DEV")

ALLOWED_HOSTS = [
    env("ALLOWED_HOST", default=None),
    "127.0.0.1",
    "localhost",
    "lony-api-3e20bf0b1e37.herokuapp.com",
    "giraffe-smashing-optionally.ngrok-free.app",
]

# CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://giraffe-smashing-optionally.ngrok-free.app",
    "https://lonyapp-2af3ad54852f.herokuapp.com",
]

CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "accept",
    "origin",
    "user-agent",
    "x-csrftoken",
]

REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "dj_rest_auth.serializers.LoginSerializer",
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "corsheaders",
    "cloudinary",
    "cloudinary_storage",
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "profiles",
    "posts",
    "comments",
    "likes",
    "followers",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "drf_api.urls"

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

WSGI_APPLICATION = "drf_api.wsgi.application"

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=str(BASE_DIR / "db.sqlite3"),
            conn_max_age=600,
            conn_health_checks=True,
        ),
    }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination."
        "PageNumberPagination"
    ),
    "PAGE_SIZE": 10,
    "DATETIME_FORMAT": "%d %b %Y",
}

REST_AUTH_TOKEN_MODEL = None

if not DEV:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
    ]

REST_USE_JWT = True
# JWT_AUTH_COOKIE = "my-app-auth"
# JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"
# JWT_AUTH_SECURE = True
# JWT_AUTH_SAMESITE = "None"

# if (
#     env("ACCESS_TOKEN_LIFETIME", default=None)
#     and env("REFRESH_TOKEN_LIFETIME", default=None)
# ):

SIMPLE_JWT = {
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ACCESS_TOKEN_LIFETIME": timedelta(
        seconds=env.int("ACCESS_TOKEN_LIFETIME", default=300)
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        seconds=env.int("REFRESH_TOKEN_LIFETIME", default=86400)
    ),
}

# in case of non-JWT endpoints
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_TRUSTED_ORIGINS = [
    "https://lonyapp-2af3ad54852f.herokuapp.com",
    "http://localhost:3000",
]
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = "None"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
