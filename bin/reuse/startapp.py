#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/startapp.py
##

"""
Usage: startapp [OPTIONS] appname [directory]

Creates a reusable django application in the directory specified, and
configures it to abide by django best practices for reusable applications.

If directory is specified, it becomes the root directory of the application.
If directory exists and creating the application would overwrite any files in
that directory, an error will be reported and no action performed.

If directory is not specified, the application will be created in a new
directory called 'django-appname', where appname is the application name
specified.  An error will be reported and no action performed if
'django-appname' already exists.

Options:
   -h        Show this help message and exit.
  --help
  --usage
"""

##
# Boilerplate
import os
import sys
script     =                  sys.argv[1]
scriptbase = os.path.basename(sys.argv[1])
subcommand = os.path.basename(sys.argv[0])
subcommand = subcommand[:-len(".py")]
del sys.argv[1]

ARGS = { "script":     scriptbase,
         "subcommand": subcommand }

##
# Handle options
import getopt
if __name__ == "__main__":
    try:
        sopts = "h"
        lopts = ["help",
                 "usage"]
        args, opts = getopt.gnu_getopt(sys.argv[1:],sopts,lopts)
    except getopt.GetoptError, exc:
        if len(exc.opt) > 1:
            ARGS["opt"] = "".join(["--",exc.opt])
        else:
            ARGS["opt"] = "".join([ "-",exc.opt])
        print ("""
%(subcommand)s: unrecognized option \'%(opt)s\'.
"""% ARGS).strip()
        print ("""
%(subcommand)s: try \'%(script)s help %(subcommand)s\' for more information.
"""% ARGS).strip(); sys.exit(-1)

#    if len(sys.argv) < 1:
#        for opt in sys.argv[1:]:
#            ARGS["opt"] = opt

##
# End of File
##
