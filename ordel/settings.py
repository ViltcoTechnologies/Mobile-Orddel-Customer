"""
Django settings for ordel project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3&6_2w!n-d*na4@a(p-us406+b4!6^xle2993x!^lefg_^*t&s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['77.68.5.32']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rest_passwordreset',
    'django_crontab',

    # Django Apps
    'order',
    'ordel',
    'payment',
    'products',
    'admin_dashboard',
    'client_app',
    'delivery_app',

    # REST_FRAMEWORK
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_tracking',
    'storages',
    'django_email_verification',
    'fcm_django',

    # Extensions
    'django_extensions',
    'django_seed',
    'axes',
    'reset_migrations',  # https://pypi.org/project/django-reset-migrations/
    'imagekit',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware'
]

CRONJOBS = [
    ('* * * * *', 'products.cron.update_avg_price_job', '> /home/orddel/orddel-cron.log'),
    ('0 */2 * * *', 'order.cron.send_pending_order_notification', '> /home/orddel/orddel-cron.log'),
    ('0 */2 * * *', 'order.cron.send_inprogress_order_notification', '> /home/orddel/orddel-cron.log')

]
CRONTAB_COMMAND_SUFFIX = '2>&1'

ROOT_URLCONF = 'ordel.urls'

EMAIL_TEMPLATE_PATH = os.path.join(BASE_DIR, 'mail_body.html')
EMAIL_SUCCESS_TEMPLATE = os.path.join(BASE_DIR, 'confirm_template.html')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ordel.wsgi.application'

# REST FRAMEWORK
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    #
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25
}

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AAAAEdSwBq8:APA91bG85e6LgqIu7vUsEmGyjwcv61AW7-d3jYDK5YjYkzzrvaLS8kUtvGeYdRS4uiB_4rEkZ77g4nhJcU3OJjfkZrN3dOPjF-PankIW2UVVI0jgnFavtGZpPA8dki2BrSBEOYKlGady"
}


AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'ordel.backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'axes.backends.AxesBackend'
]

AXES_ENABLED = False
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orddel',
        'USER': 'postgres',
        'PASSWORD': 'postgres123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=4),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# Email configuration
EMAIL_ACTIVE_FIELD = 'is_active'
# EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_SERVER = 'mail.orddel.co.uk'
# EMAIL_SERVER = 'mail.viltco.com'
# EMAIL_ADDRESS = 'leadarc123@gmail.com'
EMAIL_ADDRESS = 'support@orddel.co.uk'
# EMAIL_ADDRESS = 'orddel@viltco.com'
EMAIL_FROM_ADDRESS = 'support@orddel.co.uk'
EMAIL_PASSWORD = 'Orddel@4321'
# EMAIL_PASSWORD = '9WiPy98qhUPBvFL' # os.environ['password_key'] suggested
# EMAIL_PASSWORD = 'orddel@3221'  # os.environ['password_key'] suggested
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = EMAIL_TEMPLATE_PATH
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_PAGE_TEMPLATE = EMAIL_SUCCESS_TEMPLATE
EMAIL_PAGE_DOMAIN = 'http://77.68.5.32'


# Reset password SMTP configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'mail.viltco.com'
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST = 'smtp.orddel.co.uk'
EMAIL_PORT = 587
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'orddel@viltco.com'
# EMAIL_HOST_USER = 'leadarc123@gmail.com'
EMAIL_HOST_USER = 'support@orddel.co.uk'
# EMAIL_HOST_PASSWORD = '9WiPy98qhUPBvFL'
EMAIL_HOST_PASSWORD = 'Orddel@4321'
# EMAIL_HOST_PASSWORD = 'orddel@3221'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False


STATIC_URL = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = STATIC_URL

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# AWS_ACCESS_KEY_ID = 'AKIAYD4FFDBGKS2T7FSP'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'orddel-frontend'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# AWS_S3_REGION_NAME = 'us-east-2'
# AWS_S3_SIGNATURE_VERSION = 's3v4'

# Twilio Account
# TWILIO_ACCOUNT_SID = "AC8d6c1e71edeb9459705b7320568df7ca"
# TWILIO_AUTH_TOKEN = "4c992942b54cc4c0b88cf857cad5c200"
# SERVICE_SID = "VA98a469ee1743df522f3d0a89df50556c"
TWILIO_ACCOUNT_SID = "AC1bff27816a73d875efc57d1a54eaf7f1"
TWILIO_AUTH_TOKEN = "46049db1db0055d84ca56824c7a18b21"
SERVICE_SID = "VA7bf9da7b14d553e1e4f4bf0d77fb8bdc"

# Stripe API Keys Test

# --------------------- orddel@viltco.com -----------------------------
# Test
# STRIPE_PUBLISHABLE_KEY = 'pk_test_51IVGKwDfezRTPDs34lUTyxAmb2chp2zcCZpEbMwV7NkZWRufIcMJj3EILXrCcYZtWRFFtn34s0cWy6dE4wkSAhiF00425cFai7'
# STRIPE_SECRET_KEY = 'sk_test_51IVGKwDfezRTPDs3rwZEwqnKVGp6o9ehpuOIQyCJ5opnwQ6Bwi6O9HBVx2x48sTpjRkDZt4e2EPuSUrfKtfpLyKj00g1s0RcGH'

# --------------------- orddel.uk@gmail.com ----------------------------
# Test
STRIPE_PUBLISHABLE_KEY = 'pk_test_51IyCptIcReLPdril50b0zXIgmlquL8SUKEM00WsJdQ6x4Su2YPQ723x0Xw6cGFRCoraL3zCXICFtzSABqAzYYS9s00ctf3AVsi'
STRIPE_SECRET_KEY = 'sk_test_51IyCptIcReLPdrilpb98tUDvHF4Z4PAVFIfkWZhodB729S9YxhJjBNL8Q5KrgIfxWPO3eNr9i6DGCYOzggIRFFnD0075P0Cn7c'

# Live
# STRIPE_PUBLISHABLE_KEY = 'pk_live_51IyCptIcReLPdrilf8PHenT8O8oWbysA8eElZM2raDRwVhk9NNjvk0MCViI4fc27KEBp4Pzp8JEkaNqRU4BckBSD00ell4k13f'
# STRIPE_SECRET_KEY = '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'

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880