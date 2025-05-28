
from pathlib import Path
import environ
import dj_database_url
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    DEV=(bool, False),
)
env_file = BASE_DIR / ".env"
if env_file.exists():
    env.read_env(env_file)

CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": env("CLOUDINARY_URL"),
}
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)

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

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://giraffe-smashing-optionally.ngrok-free.app",
    "https://lonyapp-2af3ad54852f.herokuapp.com",
]

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
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "profiles",
    "posts",
    "comments",
    "likes",
    "followers",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
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
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",
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
            "ENGINE":
                "django.db.backends.sqlite3",
            "NAME":
                BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default":
            dj_database_url.config(
                default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
                conn_max_age=600,
                conn_health_checks=True,
            ),
    }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
        if DEV
        else
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE":
        10,
    "DATETIME_FORMAT":
        "%d %b %Y",
}

if not DEV:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
    ]

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"
JWT_AUTH_SAMESITE = "None"

if (
    env("ACCESS_TOKEN_LIFETIME", default=None)
    and env("REFRESH_TOKEN_LIFETIME", default=None)
):
    SIMPLE_JWT = {
        "ROTATE_REFRESH_TOKENS": True,
        "BLACKLIST_AFTER_ROTATION": True,
        "ACCESS_TOKEN_LIFETIME":
            timedelta(seconds=env("ACCESS_TOKEN_LIFETIME")),
        "REFRESH_TOKEN_LIFETIME":
            timedelta(seconds=env("REFRESH_TOKEN_LIFETIME")),
    }

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
CSRF_TRUSTED_ORIGINS = [
    "https://lonyapp-2af3ad54852f.herokuapp.com",
]

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER":
        "drf_api.serializers.CurrentUserSerializer",
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
