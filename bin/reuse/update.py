#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/update.py
##

"""
docstring for update.py
"""

##
# Boilerplate
import os
import sys
script     = os.path.basename(sys.argv[1])
subcommand = os.path.basename(sys.argv[0])
subcommand = subcommand[:-len(".py")]
del sys.argv[1]

ARGS = { "script":     script,
         "subcommand": subcommand }

from subprocess import call
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for opt in sys.argv[1:]:
            ARGS["opt"] = opt
            print ("""
%(subcommand)s: unrecognized option \'%(opt)s\'.
"""% ARGS).strip()
        print ("""
%(subcommand)s: try \'%(script)s help %(subcommand)s\' for more information.
"""% ARGS).strip(); sys.exit(-1)

    apps_dir = os.path.abspath('.')
    for app_name in os.listdir(apps_dir):
        app_dir = os.path.abspath(os.path.join(apps_dir, app_name))
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
