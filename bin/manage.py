#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/manage.py
#
# An interface to django-admin.py which adds capability to manage reusable
# django applications, application dependencies, projects which use reusable
# applications, and the creation of a development environment that encourages
# and supports reusability.
#
# We do this by replacing existing commands and hooking in new ones using the
# django command extensions mechanism.
##

import sys

COPYRIGHT     = "2009"
VERSION_BUILD = "1"
VERSION_MAJOR = "0"
VERSION_MINOR = "0"
VERSION_PATCH = "0"
VERSION_SHORT = ".".join((VERSION_MAJOR,VERSION_MINOR,VERSION_PATCH))
VERSION_LONG  = "-".join((VERSION_SHORT,VERSION_BUILD))

DJANGO_FOUND = False # A terrible hack
DJANGO_EXTENSIONS_FOUND = False
DJANGO_REUSE_FOUND = False
def try_execute_manager():
    global DJANGO_FOUND
    if DJANGO_FOUND == False:
        try:
            from django.core.management import execute_manager
            try:
                import project.settings as settings
            except:
                from django.conf import settings
                settings.configure(INSTALLED_APPS=())
            DJANGO_FOUND = True
            if DJANGO_EXTENSIONS_FOUND == True:
                settings.INSTALLED_APPS += ('django_extensions',)
            if DJANGO_REUSE_FOUND == True:
                settings.INSTALLED_APPS += ('reuse',)
            execute_manager(settings)
        except:
            pass

##
# Guard against unintended imports
if __name__ == "__main__":

 import os
 script      = os.path.realpath(__file__)
 script_base = script[:-len(".py")]
 script_dir  = os.path.dirname(script)
 dev_root    = os.path.join(script_dir,'..','..')

##
# Django command extensions are used to extend the capability of Django's
# built-in django-admin.py.  By default we use a suite of community provided
# extensions, as well as our own extensions targetted at reusable application
# development.

 import sys

 ext_path = os.path.join(dev_root,'django-extensions')
 if os.path.isdir(ext_path):
     sys.path.insert(0,ext_path)
     DJANGO_EXTENSIONS_FOUND = True

 ext_path = os.path.join(dev_root,'django-reuse')
 if os.path.isdir(ext_path):
     sys.path.insert(0,ext_path)
     DJANGO_REUSE_FOUND = True

##
# See if we're called from the context of a project, or if Django is installed
# on the default python path, and launch the command manager.

 DIRNAME = os.path.abspath(os.path.dirname(__file__))
 sys.path.insert(0, DIRNAME)
 sys.path.insert(0, os.path.join(DIRNAME, 'project'))
 try_execute_manager()
 sys.path.pop(0)
 sys.path.pop(0)

##
# Otherwise we'll try to find a stable version of Django under the assumption
# that this script is being called from a development environment that
# resembles one created by the bootstrap script.

 versions = ["final", "rc", "beta", "alpha", "trunk"]
 dev_dirs = [x for x in os.listdir(dev_root) if os.path.isdir(os.path.join(dev_root,x))]
 # Look for a django source tree, and try executing the django command line
 # admin interface.
 for ver in versions:
     for dir in [x for x in dev_dirs if ver in x]:
         sys.path.insert(0,os.path.join(dev_root,dir))
         try_execute_manager()

##
# End of File
##
