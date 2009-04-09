#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/update.py
##

"""
docstring for update.py
"""

import sys
import getopt

import os
import os.path
from subprocess import call

def update():
    apps_dir = os.path.abspath('.')
    for app_name in os.listdir(apps_dir):
        app_dir = os.path.abspath(os.path.join(apps_dir, app_name))
        git_path = os.path.join(app_dir, '.git')
        svn_path = os.path.join(app_dir, '.svn')
        mtn_path = os.path.join(app_dir, '_MTN')
        hg_path  = os.path.join(app_dir, '.hg')
        if os.path.lexists(svn_path):
            print "Updating svn %s" % app_dir
            os.chdir(app_dir)
            call(['svn', 'update'])
        elif os.path.lexists(git_path):
            print "Updating git %s" % app_dir
            os.chdir(app_dir)
            call(['git', 'pull'])
        elif os.path.lexists(mtn_path):
            print "Updating mtn %s" % app_dir
            os.chdir(app_dir)
            call(['mtn', 'pull'])
            call(['mtn', 'update'])
        elif os.path.lexists(hg_path):
            print "Updating hg %s" % app_dir
            os.chdir(app_dir)
            call(['hg', 'pull'])
            call(['hg', 'update'])
        else:
            continue

if __name__ == "__main__":
    pass

##
# End of File
##
