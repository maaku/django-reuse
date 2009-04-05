#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse.py
##

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

COPYRIGHT="2009"
VERSION_BUILD="1"
VERSION_MAJOR="0"
VERSION_MINOR="0"
VERSION_PATCH="0"
VERSION_SHORT=".".join((VERSION_MAJOR,VERSION_MINOR,VERSION_PATCH))
VERSION_LONG="-".join((VERSION_SHORT,VERSION_BUILD))

def usage():
    print """
Usage: %(basename)s <command> [options]
Try \'%(basename)s --help\' for more information.
""" % { "basename":  sys.argv[0] }; sys.exit(0)

def help():
    print """
Usage: %(basename)s <command> [options]

Options:
  -h         Display a short usage statement and exit.  All other arguments
             except \'--help\' are ignored.

  --help     Display this help message and exit.  All other arguments are
             ignored.

  --version  Display copyright and version information and then exit.  All
             other arguments except \'-h\', \'--help\', and \'--license\' are
             ignored.

  --license  Display copyright and license then exit.  All other arguments
             except \'-h\' and \'--help\' are ignored.

If \'-h\', \'--help\', \'--version\', or \'--license\' is specified, no action is
performed, regardless of any other parameters that may also be specified.
""" % { "basename":  sys.argv[0] }; sys.exit(0)

def version():
    print """
%(basename)s - Django Reusability Tool - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3
Try \'%(basename)s --license\' for more information.
""" % { "basename":  sys.argv[0],
        "version":   VERSION_LONG,
        "copyright": COPYRIGHT }; sys.exit(0)

def license():
    print """
%(basename)s - Darknet Client Application - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3

%(license)s
""" % { "basename":  sys.argv[0],
        "version":   VERSION_LONG,
        "copyright": COPYRIGHT,
        "license":   "FIXME" }; sys.exit(0)

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "version", "license"])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)

    ##
    # Handle command line arguments and options.
    opt_h       = False
    opt_help    = False
    opt_version = False
    opt_license = False
    for opt, arg in opts:
        if opt=="-h":        opt_h       = True
        if opt=="--help":    opt_help    = True
        if opt=="--version": opt_version = True
        if opt=="--license": opt_license = True

    if opt_help:    help()
    if opt_h:       usage()
    if opt_license: license()
    if opt_version: version()

    for arg in args:
        print arg

    print os.path.dirname(__file__)

##
# End of File
##
