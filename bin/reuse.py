#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse.py
##

##
# For ease of maintainability, the functionlity of django-reuse.py is split
# across the bin/reuse module.  So the first thing we need to do is add this
# module to PYTHONPATH.  A little bit of sys.path magic is all that's
# required.
import os
import sys
script_name = __file__
script_path = os.path.dirname(__file__)
script_full = os.path.join(script_path, script_name)
script      = os.path.realpath(script_full)
script_base = script[:-len(".py")]
sys.path.append(script_base)

##
#
import reuse
ARGS = { "basename":  sys.argv[0],
         "copyright": reuse.COPYRIGHT,
         "version":   reuse.VERSION_LONG,
         "license":   "FIXME" }

def usage():
    print """
Usage: %(basename)s <command> [options]
Try \'%(basename)s --help\' for more information.
""".strip() % ARGS; sys.exit(0)

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
""".strip() % ARGS; sys.exit(0)

def version():
    print """
%(basename)s - Django Reusability Tool - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3
Try \'%(basename)s --license\' for more information.
""".strip() % ARGS; sys.exit(0)

def license():
    print """
%(basename)s - Darknet Client Application - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3

%(license)s
""".strip() % ARGS; sys.exit(0)

##
#　Handle basic usage- and info-related commands.
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "version", "license"])
except getopt.GetoptError:
    usage()
    sys.exit(-1)

opt_h       = False
opt_help    = False
opt_version = False
opt_license = False
for opt, arg in opts:
    if opt=="-h":        opt_h   = True
    if opt=="--help":    opt_help= True
    if opt=="--version": opt_version = True
    if opt=="--license": opt_license = True

if opt_help:    help()
if opt_h:       usage()
if opt_license: license()
if opt_version: version()

##
# End of File
##
