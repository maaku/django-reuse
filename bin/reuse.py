#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse.py
#
# A tool for managing reusable django applications, application dependencies,
# projects which use reusable applications, and the creation of a development
# environment that encourages and support reusability.
##

COPYRIGHT     = "2009"
VERSION_BUILD = "1"
VERSION_MAJOR = "0"
VERSION_MINOR = "0"
VERSION_PATCH = "0"
VERSION_SHORT = ".".join((VERSION_MAJOR,VERSION_MINOR,VERSION_PATCH))
VERSION_LONG  = "-".join((VERSION_SHORT,VERSION_BUILD))

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
sys.path.insert(0,script_base)

licname = os.path.join(script_base,"..","..","COPYING.txt")
try:
    licfile = open(licname, 'r')
    license = licfile.read()
    licfile.close()
except:
    license = "Error reading license file %s..." % licname

##
#
ARGS = { "basename":  os.path.basename(sys.argv[0]),
         "copyright": COPYRIGHT,
         "version":   VERSION_LONG,
         "license":   license }

def usage():
    print ("""
Usage: %(basename)s <command> [options]
Try \'%(basename)s --help\' for more information.
"""% ARGS).strip(); sys.exit(0)

def help():
    print ("""
Usage: %(basename)s <command> [options]

Options:
   -h        Display a short usage statement and exit.  All other arguments
  --usage    except \'--help\' are ignored.

  --help     Display this help message and exit.  All other arguments are
             ignored.

  --version  Display copyright and version information and then exit.  All
             other arguments except \'-h\'/\'--usage\', \'--help\', and \'--license\'
             are ignored.

  --license  Display copyright and license then exit.  All other arguments
             except \'-h\'/\'--usage\' and \'--help\' are ignored.

If \'-h\', \'--usage\', \'--help\', \'--version\', or \'--license\' is specified, no
action is performed, regardless of any other parameters that may also be
specified.
"""% ARGS).strip(); sys.exit(0)

def version():
    print ("""
%(basename)s - Django Reusability Tool - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3
Try \'%(basename)s --license\' for more information.
"""% ARGS).strip(); sys.exit(0)

def license():
    print ("""
%(basename)s - Django Reusability Tool - version %(version)s
Copyright (c) %(copyright)s by its contributors and distributed
under the terms of the GNU Affero General Public License, version 3

%(license)s
"""% ARGS).strip(); sys.exit(0)

##
#　Handle basic usage- and info-related commands.
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "h", ["usage", "help", "version", "license"])
except getopt.GetoptError:
    usage()
    sys.exit(-1)

opt_h       = False
opt_help    = False
opt_version = False
opt_license = False
for opt, arg in opts:
    if opt=="-h":        opt_h       = True
    if opt=="--usage":   opt_h       = True
    if opt=="--help":    opt_help    = True
    if opt=="--version": opt_version = True
    if opt=="--license": opt_license = True

if opt_help:    help()
if opt_h:       usage()
if opt_license: license()
if opt_version: version()

##
# End of File
##
