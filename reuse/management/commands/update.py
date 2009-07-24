#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/update.py
##

"""
docstring for update.py
"""

# ##
# # Boilerplate
# import os
# import sys
# script     =                  sys.argv[1]
# scriptbase = os.path.basename(sys.argv[1])
# subcommand = os.path.basename(sys.argv[0])
# subcommand = subcommand[:-len(".py")]
# del sys.argv[1]
#
# ARGS = { "script":     scriptbase,
#          "subcommand": subcommand }
#
# from subprocess import call
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         for opt in sys.argv[1:]:
#             ARGS["opt"] = opt
#             print ("""
# %(subcommand)s: unrecognized option \'%(opt)s\'.
# """% ARGS).strip()
#         print ("""
# %(subcommand)s: try \'%(script)s help %(subcommand)s\' for more information.
# """% ARGS).strip(); sys.exit(-1)

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
