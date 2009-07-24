#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/update.py
##

"""
docstring for update.py
"""

from django.core.management.base import NoArgsCommand

import os
from subprocess import call

class Command(NoArgsCommand):
    help = "Updates git, svn, mtn, and hg repositoreis."

    requires_model_validation = False

    def handle_noargs(self, **options):
        dev_dir = os.path.abspath('.')
        for app_name in os.listdir(dev_dir):
            app_dir = os.path.abspath(os.path.join(dev_dir, app_name))
            if os.path.lexists(os.path.join(app_dir,'.svn')):
                print "Updating svn %s" % app_dir
                os.chdir(app_dir)
                call(['svn', 'update'])
            elif os.path.lexists(os.path.join(app_dir,'.git')):
                print "Updating git %s" % app_dir
                os.chdir(app_dir)
                call(['git', 'pull'])
            elif os.path.lexists(os.path.join(app_dir,'_MTN')):
                print "Updating mtn %s" % app_dir
                os.chdir(app_dir)
                call(['mtn', 'pull'])
                call(['mtn', 'update'])
            elif os.path.lexists(os.path.join(app_dir,'.hg')):
                print "Updating hg %s" % app_dir
                os.chdir(app_dir)
                call(['hg', 'pull'])
                call(['hg', 'update'])
            else:
                continue

##
# End of File
##
