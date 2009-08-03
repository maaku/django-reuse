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

DJANGO_FOUND = False # A terrible hack
DJANGO_EXTENSIONS_FOUND = False
DJANGO_REUSE_FOUND = False
def try_execute_manager():
    global DJANGO_FOUND
    if DJANGO_FOUND == False:
        try:
            from django.core.management import execute_manager
            try:
                from project import settings
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
 script   = os.path.realpath(__file__)
 bin_dir  = os.path.dirname(script)
 dev_root = os.path.join(bin_dir,'..','..')

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

 if os.path.isfile(os.path.join('.','django','bin','django-admin.py')) and os.path.isfile(os.path.join('.','project','settings.py')):
     DIRNAME = os.path.abspath(os.path.dirname(__file__))
     sys.path.insert(0, DIRNAME)
     sys.path.insert(0, os.path.join(DIRNAME, 'apps'))
     sys.path.insert(0, os.path.join(DIRNAME, 'project'))

     from django.core.management import execute_manager
     from project import settings

     if DJANGO_EXTENSIONS_FOUND == True:
         settings.INSTALLED_APPS += ('django_extensions',)
     if DJANGO_REUSE_FOUND == True:
         settings.INSTALLED_APPS += ('reuse',)

     execute_manager(settings)
     sys.exit(0)

##
# Otherwise we'll try to find a stable version of Django under the assumption
# that this script is being called from a development environment that
# resembles one created by the bootstrap script.

 # temp is a bad name.. but it is a variable that has a lot of different uses
 # in the following code (maybe 'misc' would be better?).  By the time we get
 # to "if len(temp) > 0", temp is a list of potential Django installations.
 temp = []

 # If there is a django installation (or a symlink to one) by the name of
 # 'django' in the development directory, use that.
 if os.path.isfile(os.path.join(dev_root,'django','bin','django-admin.py')):
     temp = ['.']
 # Otherwise collect all potential Django installations in the current
 # directory (test by checking for the existance of django-admin.py) and
 # crudely sort by release type.
 else:
     # Build list of Django candidate installations.
     temp = [x for x in os.listdir(dev_root) if os.path.isdir(os.path.join(dev_root,x))]
     dirs = [x for x in temp if os.path.isfile(os.path.join(x,'django','bin','django-admin.py'))]
     # Sort that list by stability and version number.  The result is a list
     # sorted by stability ('final' first, 'trunk' last) and subsorted by
     # reverse alphabetic order, which *should* result in descending version
     # numbers.
     vers = ["final", "rc", "beta", "alpha", "trunk"]
     temp = map(lambda ver: [x for x in dirs if ver in x], vers)
     map(lambda dirs: dirs.sort(reverse=True), temp)
     temp = [x for y in temp for x in y]

 # If there's still no Django installation found... perhaps it's in the python
 # path?
 if not temp:
     try:
         import django
         # Give temp something to be put back on the python path.
         temp = [sys.path.pop(0)]
     except:
         pass

 # Use the highest version of the most stable category of release available.
 if len(temp) > 0:
     sys.path.insert(0,os.path.join(dev_root,temp.pop(0)))

     from django.core.management import execute_manager
     from django.conf import settings

     settings.configure(INSTALLED_APPS=())
     if DJANGO_EXTENSIONS_FOUND == True:
         settings.INSTALLED_APPS += ('django_extensions',)
     if DJANGO_REUSE_FOUND == True:
         settings.INSTALLED_APPS += ('reuse',)

     execute_manager(settings)
     sys.exit(0)

 # No Django installation... epic fail.
 else:
     sys.stderr.write("""
error: Could not find Django installation.  Are you sure that your development
error: environment is setup correctly?
""".lstrip())
     sys.exit(1)

##
# End of File
##
