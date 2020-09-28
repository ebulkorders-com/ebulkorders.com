"""
Django settings for infiniteshop project.

Generated by 'django-admin startproject' using Django 3.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2z8@$p@o=lo3n2c6&^(jvrcmgbtj1)2g7ak$6kpqz^9_(rp)fi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sites',
            'django.contrib.flatpages',
            'oscar',
            'oscar.apps.analytics',
            'oscar.apps.communication',
            'oscar.apps.checkout',
            'oscar.apps.address',
            'oscar.apps.shipping',
            'oscar.apps.catalogue',
            'oscar.apps.catalogue.reviews',
            'oscar.apps.partner',
            'oscar.apps.basket',
            'oscar.apps.payment',
            'oscar.apps.offer',
            'oscar.apps.order',
            'oscar.apps.customer',
            'oscar.apps.search',
            'oscar.apps.voucher',
            'oscar.apps.wishlists',
            'oscar.apps.dashboard',
            'oscar.apps.dashboard.reports',
            'oscar.apps.dashboard.users',
            'oscar.apps.dashboard.orders',
            'oscar.apps.dashboard.catalogue',
            'oscar.apps.dashboard.offers',
            'oscar.apps.dashboard.partners',
            'oscar.apps.dashboard.pages',
            'oscar.apps.dashboard.ranges',
            'oscar.apps.dashboard.reviews',
            'oscar.apps.dashboard.vouchers',
            'oscar.apps.dashboard.communications',
            'oscar.apps.dashboard.shipping',
            # 3rd-party apps that oscar depends on
            'widget_tweaks',
            'haystack',
            'treebeard',
            'sorl.thumbnail',
            'django_tables2',
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
# oscar middleware
'oscar.apps.basket.middleware.BasketMiddleware',
'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
'oscar.apps.customer.auth_backends.EmailBackend',
'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'ebulkorders.urls'

HAYSTACK_CONNECTIONS = {
   'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
   },
}

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
                # oscars context processors
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
],
        },
    },
]

WSGI_APPLICATION = 'ebulkorders.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
