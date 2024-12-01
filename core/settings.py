import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$*r+l*b2dxn-j-rk=r57ejwy575^g_x^+ac9a2jc&&w$&99mc&"

# WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "bootstrap5",
    "django_htmx",
    "storages",
]

MAIN_APPS = [
    "mainapps.video",
    "mainapps.home",
    "mainapps.accounts",
    "mainapps.vidoe_text",
    "mainapps.audio",
]

INSTALLED_APPS = []
INSTALLED_APPS.extend(DEFAULT_APPS)
INSTALLED_APPS.extend(THIRD_PARTY_APPS)
INSTALLED_APPS.extend(MAIN_APPS)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "vlcdb1",
        "USER": "ubongpr7",
        # "PASSWORD": os.getenv("DB_PASSWORD"),
        "PASSWORD": "ubongpr7",
        "HOST": "vlcdb1.cp8w6cg80sxf.eu-north-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 6,
        },
    },
]
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

LANGUAGE_CODE = "en-us"
USE_I18N = True
TIME_ZONE = "UTC"
USE_TZ = True

# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DOMAIN_NAME = 'http://153.92.208.98:8000'
DOMAIN_NAME = 'http://91.108.112.100:7732'
# DOMAIN_NAME = "http://localhost:8000"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = "static/"  # This will be overridden for S3
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_URL = "media/"  # This will be overridden for S3
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "vlsmlsaker"
AWS_S3_REGION_NAME = "eu-north-1"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILES_OVERWRITE = False

# DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
# if DEBUG:
#     STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage"
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     }
#     }
# else:
#     STORAGES = {
#         "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
#         "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
#     }


STORAGES = {
        "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
        "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
}

PASSWORD_RESET_TIMEOUT = 3600 * 24

GROWTH_PLAN_PRICE_ID = "price_1QFL9dCE1QRwCUcQI7m2u0Qo"
PRO_PLAN_PRICE_ID = "price_1QFLBPCE1QRwCUcQAVEn9Fzc"

STRIPE_PUP_KEY = "pk_test_51QFJH8CE1QRwCUcQ4SUDaXgVIecDWTgspSuAigMWEqkCLSQKUNOwDAFhKz8gQNTQUo906g3skCLH3VIbtqW3WvfC00G2OzUfGL"
STRIPE_SEC_KEY = "sk_test_51QFJH8CE1QRwCUcQQXoD8234vq5shQrDdYSKE2W6YXGuEHVkfMw95MKmtxWl5r937vk3iAkE8F1Ru6v6gU9BEACN00Ebnug6ws"
STRIPE_ENDPOINT_SECRET = "whsec_qHxFoupL1x85MVIckw4ltWNSc8tFpK1L"
# STRIPE_ENDPOINT_SECRET = 'whsec_bcb1c431b23c3f902f4b28786651f11b9ecef0e023b737880df90e0ccb1e6e6c'
