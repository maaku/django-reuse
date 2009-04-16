#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/startproject.py
##

"""
Usage: startproject [OPTIONS] projectname [directory]

Creates a django project in the directory specified, and configures the
project to abide by django best practices and to make the integration of
reusable applications easier.

If directory is specified, it becomes the root directory of the project.  If
directory exists and creating the project would overwrite any files in that
directory, an error will be reported and no action performed.

If directory is not specified, the project will be created in a new directory
called 'site-projectname', where projectname is the project name specified.
An error will be reported and no action performed if 'site-projectname'
already exists.

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
# End of File
##
