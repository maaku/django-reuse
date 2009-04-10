#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: bin/reuse/help.py
##

"""
docstring for help.py
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
# Parse command line
import getopt
try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], "")
except getopt.GetoptError, exc:
    ARGS["opt"] = exc.opt
    print ("""
%(subcommand)s: unrecognized option \'%(opt)s\'.
"""% ARGS).strip(); sys.exit(-1)

if len(args) > 1:
    for arg in args[1:]:
        ARGS["arg"] = arg
        print ("""
%(subcommand)s: unexpected argument \'%(arg)s\'.
"""% ARGS).strip()
    sys.exit(-1)

##
# Handle case of no topic specified.
from subprocess import call
if len(args) < 1:
    call(["python",script,"--help"])
    sys.exit(0)

##
# Finally, handle the case of asking for help on a particular topic.
import compiler
topic = args[0].strip().lower()
filename = os.path.join(os.path.dirname(__file__),
                        "".join([topic,".py"]))
try:
    source = open(filename).read()
except IOError:
    ARGS["topic"] = topic
    print ("""
%(subcommand)s: command \'%(topic)s\' does not exist.
%(subcommand)s: try \'%(script)s help\' for a list of commands.
"""% ARGS).strip()
    sys.exit(-1)
call(["python",script,"--version"])
print ""
print compiler.parse(source).doc.strip()

##
# End of File
##
