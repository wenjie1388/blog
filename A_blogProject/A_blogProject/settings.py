import os
from pathlib import Path
from A_blogProject.pro import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ctc$6quh7wt_*dz&r#p!@#g)=1cs4f3bqr2%w^50^43fgz1g!7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG_

ALLOWED_HOSTS = []
APPEND_SLASH = False
# AUTH_USER_MODEL = 'django.contrib.auth.models.User'
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "article.apps.ArticleConfig",
    "consumer.apps.ConsumerConfig",
    "auths.apps.AuthsConfig",
    "rest_framework",
    "corsheaders",
]


MIDDLEWARE = [
    # 跨域中间件
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "A_blogProject.urls"

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

WSGI_APPLICATION = "A_blogProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": MYSQLNAME,
        "USER": MYSQLUSER,
        "PASSWORD": MYSQLPASSWORD,
        "HOST": MYSQLHOST,
        "PORT": MYSQLPORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/shanghai"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# 文件和图片上传配置
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
# "/media/"
MEDIA_URL = "media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# *===============================================* #
# ******************** 跨域配置 ******************** #
# *===============================================* #

CORS_ALLOW_CREDENTIALS = True  # 允许携带cookies
CORS_ORIGIN_ALLOW_ALL = True

# 跨域白名单
CORS_ORIGIN_WHITELIST = [
    "127.0.0.1:5173",
    "127.0.0.1:8000",
]


CORS_ORIGIN_WHITELIST = ()
# 对应的发送的请求的跨域
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "VIEW",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)


# =============================================== #
# **************** 日志 配置 ***************** #
# =============================================== #

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    "handlers": {
        "console": {
            "level": "INFO",
            # 'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            # 'filters': ['special']
            "class": "django.utils.log.AdminEmailHandler",
        },
        "file": {
            "level": "DEBUG",
            # 'class': 'logging.FileHandler',
            "class": "logging.FileHandler",
            "filename": "log/log.txt",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            # 'handlers': ['mail_admins'],
            "handlers": [
                "file",
            ],
            # 'level': 'ERROR',
            "level": "DEBUG",
            # * propagate 是指
            "propagate": False,
        },
        "myproject.custom": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            # 'filters': ['special']
        },
    },
}


# =============================================== #
# **************** DRF 配置 ***************** #
# =============================================== #
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
}

# ============================================== #
# **************** Caches 配置 ***************** #
# =============================================== #

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS0_LOCATION,
        "OPTIONS": {
            "db": "10",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },"captcha": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS1_LOCATION,
        "OPTIONS": {
          "CONNECTION_POOL_KWARGS":{"max_connections":100}
        },
    },
}
