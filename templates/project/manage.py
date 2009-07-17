#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# project.manage
##

# Added by Mark Friedenbach 15 Jul 2009
# to support django project layout
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'project')

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the project directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)

##
# End of File
##
