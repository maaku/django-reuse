#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# manage.py
##

# Added by Mark Friedenbach 28 Jul 2009
# as a temporary stand-in until this manage.py is rewritten.  Ideally an
# application's manage.py should be able to find the manage.py of django-reuse
# and call that.
import sys
sys.stderr.write("""
error: Application manage.py has not been written yet!  Please use the
error: manage.py provided by django-reuse, or django-admin.py directly.
""".lstrip())
sys.exit(1)

# Added by Mark Friedenbach 15 Jul 2009
# to support django project layout
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'project')

try:
    from django.core.management import execute_manager
except:
    sys.stderr.write("""
error: Can't find the django.core.management module.  Are you sure that you
error: added Django to your installed python path, or a link to it in your
error: project's root directory?
""".lstrip())
    sys.exit(1)

try:
    import settings # Assumed to be in the project directory.
except ImportError:
    sys.stderr.write("""
error: Can't find the file 'settings.py' in the directory containing
error: %r.
error:
error: It appears you've customized things.  You'll have to find and run
error: django-admin.py manually, passing it your settings module.  (If the
error: file settings.py does indeed exist, it's causing an ImportError
error: somehow.)
""".lstrip() % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)

##
# End of File
##
