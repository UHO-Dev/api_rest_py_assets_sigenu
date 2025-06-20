"""
Django settings for api_rest project.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-7tlq5pt*1syqjw@w19d&c&ja!i^vhus$ijq0=02^*nzcg7mgp'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
    "django_filters",
    "rest_framework",
    "assets",
    "sigenu",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.extend(["debug_toolbar", "crispy_forms", "crispy_bootstrap3"])
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = [
        "localhost",
        "127.0.0.1",
    ]
    CRISPY_TEMPLATE_PACK = "uni_form"


ROOT_URLCONF = "api_rest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "api_rest.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "rh": {
        "ENGINE": "sql_server.pyodbc",
        "NAME": os.environ.get("DB_NAME_RH"),
        "USER": os.environ.get("DB_USER_RH"),
        "PASSWORD": os.environ.get("DB_PWD_RH"),
        "HOST": os.environ.get("DB_HOST_RH"),
        "PORT": os.environ.get("DB_PORT_RH"),
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
    "int": {
        "ENGINE": "sql_server.pyodbc",
        "NAME": os.environ.get("DB_NAME_INT"),
        "USER": os.environ.get("DB_USER_RH"),
        "PASSWORD": os.environ.get("DB_PWD_RH"),
        "HOST": os.environ.get("DB_HOST_RH"),
        "PORT": os.environ.get("DB_PORT_RH"),
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
    "sigenu_student": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME_SIGENU"),
        "USER": os.environ.get("DB_USER_SIGENU"),
        "PASSWORD": os.environ.get("DB_PASSWORD_SIGENU"),
        "HOST": os.environ.get("DB_HOST_SIGENU"),
        "PORT": os.environ.get("DB_PORT_SIGENU"),
    },
    # 'ldap': {
    #     'ENGINE': 'ldapdb.backends.ldap',
    #     'NAME': 'ldap://10.26.0.69/',
    #     'USER': 'cn=admin,dc=uho,dc=edu,dc=cu',
    #     'PASSWORD': 'temporal123',
    # },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,  # 11809
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}
