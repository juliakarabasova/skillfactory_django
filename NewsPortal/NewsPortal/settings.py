"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v8oc*hu9nv94+1k-4iykmex0lmf%(r0@s4p6k4%hfqnr!)8-y='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news.apps.NewsConfig',

    'django.contrib.sites',
    'django.contrib.flatpages',

    # 'news',
    'sign',
    'protect',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR.parent, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LOGIN_URL = '/accounts/login/'

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'juliakarabasova'
# EMAIL_HOST_PASSWORD = 'Hw4;3Thb3wpV'
EMAIL_HOST_PASSWORD = 'iygktgaoceutlrvt'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR.parent / "static"
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '748010322329-r7mkj0ugvjn8bg7cdmcg05k2jiulm7ba.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается,
# можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

# redis://:пароль@endpoint:port
CELERY_BROKER_URL = ('redis://:jzkfPAfeuMAt4RZmoaV9gT10pVfj5EXc'
                     '@redis-19646.c253.us-central1-1.gce.redns.redis-cloud.com:19646')
CELERY_RESULT_BACKEND = ('redis://:jzkfPAfeuMAt4RZmoaV9gT10pVfj5EXc'
                         '@redis-19646.c253.us-central1-1.gce.redns.redis-cloud.com:19646')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# --pool=solo


ADMINS = [
    ('Julia Karabasova', 'karabasova@veta.expert')
]

SERVER_EMAIL = DEFAULT_FROM_EMAIL


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'error': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s %(exc_info)s'
        },
        'warning': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
        'debug': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'file_info': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'admin_error': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
    },
    'filters': {
        'debug_filter': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'not_debug_filter': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['debug_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['debug_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['debug_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'error'
        },
        'file_info': {
            'level': 'INFO',
            'filters': ['not_debug_filter'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'file_info'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error'
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'file_info'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['not_debug_filter'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'admin_error'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error',
                         'file_info'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_errors'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['mail_admins', 'file_errors'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins', 'file_security'],
            'propagate': True,
        },
    }
}