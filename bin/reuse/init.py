#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/init.py
##

"""
Usage: init [directory]
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

##
# End of File
##
