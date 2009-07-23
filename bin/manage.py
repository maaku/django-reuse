#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/manage.py
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
# For ease of maintainability, the functionlity of this manage.py is split
# across the bin/reuse module.  So the first thing we need to do is add this
# module to PYTHONPATH.  A little bit of sys.path magic is all that's
# required.
import os
import sys
script      = os.path.realpath(__file__)
script_base = script[:-len(".py")]
sys.path.insert(0,script_base)

##
# The license string is read from the file COPYING.txt in the root of the
# django-reuse project directory.  The contents of this file is output in
# response to the user specified '--license' option.
licname = os.path.join(script_base,"..","..","COPYING.txt")
try:
    licfile = open(licname, 'r')
    license = licfile.read()
    licfile.close()
except:
    license = "Error reading license file %s..." % licname

##
# The functions usage(), help(), version(), and license() handle the user
# specified options '-h' and '--usage', '--help', '--version', and '--license'
# respectfully.
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

The following commands are recognized (use \'%(basename)s help <command>\'
to get detailed documentation of each command):
"""% ARGS).strip();
    import re
    print ""
    for filename in os.listdir(script_base):
        if not re.match(r"^.*.py$", filename) or filename == "__init__.py":
            continue
        print "    %s" % filename[:-len(".py")]
    sys.exit(0)

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
opt_h       = False
opt_help    = False
opt_version = False
opt_license = False
for opt in sys.argv[1:]:
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
# Extract command, removing it from the list of arguments.
cmd = None
for arg in sys.argv[1:]:
    if arg.startswith("-") != True:
        cmd = arg.strip().lower()
        sys.argv.remove(arg)
        break

##
# See if there is anything to do
if cmd == None:
    print ("""
%(basename)s: nothing to do; exiting.
%(basename)s: try \'%(basename)s --help\' for usage information.
"""% ARGS).strip(); sys.exit(0)

##
# See if command is valid (subscript exists)
subscript = os.path.join(script_base, "".join([cmd,".py"]))
if os.path.exists(subscript) != True:
    ARGS["cmd"]=cmd
    print ("""
%(basename)s: unrecognized subcommand \'%(cmd)s\'.
%(basename)s: try \'%(basename)s --help\' for a list of valid commands.
"""% ARGS).strip(); sys.exit(-1)

##
# Execute command
from subprocess import call
call_args = ["python", subscript]
call_args.extend(sys.argv)
call(call_args)

##
# End of File
##
