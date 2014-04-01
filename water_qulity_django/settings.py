# -*- coding: UTF-8 -*-
"""
Django settings for water_qulity_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')n1-ru5z_887jdml-%(@b)^a#u62_^48)f^vtlxib5v(9-m=g5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'hardsocket',
    'device',
    # 'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #add for international
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #
    # 'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'water_qulity_django.urls'

WSGI_APPLICATION = 'water_qulity_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',#'django.db.backends.postgresql_psycopg2','django.db.backends.sqlite3','django.db.backends.oracle'
        'NAME': 'water_quanlity',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        # 'PASSWORD': 'honest1101',
        # 'HOST': '192.168.8.65',
        'PORT': '3306',
    }
    # 'default': {
    #     'ENGINE':'django.db.backends.sqlite3',
    #     'NAME': os.path.join('waterqulity.db'),
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Shanghai'#'UTC'

USE_I18N = True

USE_L10N = True

#TOCO 
USE_TZ = False#True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# add by tommy
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'assets'),
    os.path.join(BASE_DIR,'my_static'),
    )
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)
# ADMIN_MEDIA_PREFIX = '/static/admin/'
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'verbose':{
            'format':'%(asctime)s %(levelname)-8s module:%(name)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters':{
    },
    'handlers':{
        'handler_console':{
            'level':'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'handler_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers':{
        'socket.crc':{
            'handlers':['handler_console'],
            'level':'INFO',
        }
    },
}