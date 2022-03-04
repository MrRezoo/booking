"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import path

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&n7shm!0su^0fw4e@i_2#r+0t@2wuhcmi+&lug(nf$gg1037qh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1', '141.11.246.38']
INTERNAL_IPS = ['127.0.0.1', '141.11.246.38']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'accounts.apps.AccountsConfig',
    'core.apps.CoreConfig',
    'club.apps.ClubConfig',
    'blog.apps.BlogConfig',
    'utils',
    # third party apps
    'rest_framework',
    'django_extensions',
    'debug_toolbar',
    'django_filters',
    'social_django',
    'storages',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "booking",
        'USER': 'postgres',
        'PASSWORD': "postgres",
        'HOST': 'localhost',
        # 'HOST': '141.11.246.38',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend'),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

# ARVAN CLOUD STORAGE
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '628445fe-1c0d-4936-9473-7fbfe2f101eb'
AWS_SECRET_ACCESS_KEY = 'b244d6478db7b15d467ded6ec176d88b9ee8c93a0e7a2ffd667993904efca216'
AWS_STORAGE_BUCKET_NAME = 'django-club'
AWS_SERVICE_NAME = 's3'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_S3_FILE_OVERWRITE = False
AWS_LOCAL_STORAGE = f"{BASE_DIR}/aws/"
# ARVAN CLOUD STORAGE


# SOCIAL DJANGO
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_GITHUB_KEY = 'baf8d8d297f87571a963'
SOCIAL_AUTH_GITHUB_SECRET = '93bc6f46fe276d0d09d4074cdffacf524958bc47'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '788032830417-fcmo7dpt37bmsmk3tfoo4gt0qdni2v7q.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'm6PdAVgi7bAu6GK5B1vV9sjC'
# SOCIAL DJANGO

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'search'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'search'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
CKEDITOR_UPLOAD_PATH = ""
CKEDITOR_RESTRICT_BY_DATE = False
