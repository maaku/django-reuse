#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# project.settings
##

##
# Standard Django settings.py boilerplate
import os
DIRNAME = os.path.dirname(os.path.realpath(__file__))

# Django settings for $PROJECT_NAME$.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('$AUTHOR_NAME$', '$AUTHOR_EMAIL$'),
)
MANAGERS = ADMINS

# Added by Mark Friedenbach 17 Jul 2009
# to support enabling admin through simple config
ADMIN = True
ADMIN_DOC = ADMIN

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''
#
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = ''

# Added by Mark Friedenbach 15 Jul 2009
# to support media serving for development purposes
import os
MEDIA_ROOT = os.path.join(DIRNAME,'..','static')
MEDIA_SERVE = True
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

# Added by Mark Friedenbach
# because the default prefix is unintuitive and blocks '/media/'
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$SECRET_KEY$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)

# Added by Mark Friedenbach 17 Jul 2009
# to enable admin with simple configuration changes
if ADMIN == True:
    INSTALLED_APPS = ('django.contrib.admin',
        ) + INSTALLED_APPS
if ADMIN_DOC == True:
    INSTALLED_APPS = ('django.contrib.admindoc',
        ) + INSTALLED_APPS

# Added by Mark Friedenbach 17 Jul 2009
# load settings specific to this host machine/production environment
try:
    from settings_local import *
except:
    pass

##
# End of File
##
