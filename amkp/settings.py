# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\amkp\settings.py
# Size of source mod 2**32: 4020 bytes
# Decompiled by https://python-decompiler.com
"""
Django settings for amkp project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from django.contrib.messages import constants as messages
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '&g)*t6x%licu1#$81d+@)6f*wcmxh3@jn5ia!zmp2z(q82o@my'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'newsletter.apps.NewsletterConfig',
    'contacts.apps.ContactsConfig',
    'articles.apps.ArticlesConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'amkp.urls'
TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
     'DIRS': [
         os.path.join(BASE_DIR, 'templates')],
     'APP_DIRS':True,
     'OPTIONS':{'context_processors': [
         'django.template.context_processors.debug',
         'django.template.context_processors.request',
         'django.contrib.auth.context_processors.auth',
         'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'amkp.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql',
                         'NAME': 'amkpdb',
                         'USER': 'postgres',
                         'PASSWORD': 'superadmin',
                         'HOST': 'localhost'}}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'amkp/static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MESSAGE_TAGS = {messages.ERROR: 'danger'}
