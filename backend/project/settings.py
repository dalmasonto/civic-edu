"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^5g2q&v1l$iit&dg$ov&*zqfv&#5b5q&zdomd-@x)1sc(7vveh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'utils',
    'account',
    'customauth',
    'main',

    # Third party apps for DRF
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_rest_passwordreset',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'main.authentication.BearerTokenAuthentication'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db1.sqlite3',
            "ATOMIC_REQUESTS": True,
        }
    }
else:
    SECURE_SSL_REDIRECT = True
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': 'rheaafri_sitedb',
            'USER': 'rheaafri_sitedb',
            'PASSWORD': 'M^D3U}I{ykx=',
            'HOST': 'localhost',
            'PORT': '3306',
            "ATOMIC_REQUESTS": True,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = 'staticfiles/'
STATICFILES_DIRS = ['static/', 'media/']

# DOMAIN SETTINGS
MY_DOMAIN = "http://localhost:8000"

if DEBUG:
    MEDIA_URL = 'media/'
    MEDIA_ROOT = 'data/media/'

    # CORS_ALLOWED_ORIGINS = []
    CORS_ALLOW_ALL_ORIGINS = True

else:
    MEDIA_ROOT = '/home/rheaafri/media.rhea.africa/'
    MEDIA_URL = 'https://media.rhea.africa/'

    CORS_ALLOWED_ORIGINS = ['https://rhea.africa', 'https://www.rhea.africa', 'http://rhea.africa',
                            'http://www.rhea.africa']
    # CORS_ALLOW_ALL_ORIGINS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# System Settings

COST_PER_TEST = {
    'basic-micro-nutrients-analysis': 2000,
    'complete-soil-analysis': 6500
}

# Main Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_PORT = 465
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
EMAIL_HOST = 'mail.rhea.africa'
EMAIL_HOST_USER = 'Rhea Africa <no-reply@rhea.africa>'
EMAIL_HOST_PASSWORD = "hLDr~_$_Z1qG"

# MailTrap Settings
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = '3c818e85681343'
# EMAIL_HOST_PASSWORD = '470191fc5ca79a'
# EMAIL_PORT = '2525'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# LOGGING
