#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/startapp.py
##

"""
docstring for startapp.py
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
