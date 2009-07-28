#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.newproject
##

"""
Usage: newproject projectname [directory]

Creates a django project in the directory specified, and configures the
project to abide by django best practices and to make the integration of
reusable applications easier.

If directory is specified, it becomes the root directory of the project.  If
directory exists and creating the project would overwrite any files in that
directory, an error will be reported and no action performed.

If directory is not specified, the project will be created in a new directory
called 'proj-projectname', where projectname is the project name specified.
An error will be reported and no action performed if 'proj-projectname'
already exists.
"""

##
# Boilerplate
from django.core.management.base import LabelCommand

import os
subcommand = os.path.basename(__file__)
subcommand = subcommand[:-len(".py")]
ARGS = { "subcommand": subcommand }

##
# dir_walk() takes a single directory as an argument and returns a list of all
# the files found by walking that directory hierarchy.  The relative paths of
# those files are included, but not the original directory.
#
# This function is used by is_safe_pdir() to see if there is any overlap
# between pdir (the user specified project directory) and tdir (the template
# directory which contains the skeleton project).
def dir_walk(dir):
    fils = []
    dirs = [dir]
    pfix = os.path.join(dir, '')
    while len(dirs)>0:
        dir = dirs.pop()
        for name in os.listdir(dir):
            # Hack: ignore any hidden files
            if name.startswith("."):
                continue
            fullpath = os.path.join(dir, name)
            if os.path.isfile(fullpath):
                fils.append(fullpath[len(pfix):])
            else:
                dirs.append(fullpath)
    return fils

def template_dir(name):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","..","..","templates",name)

##
# Checks that a directory is safe to use as the target of a directory copy
# operation.  Namely, it checks that the template directory exists, and that
# if the target directory exists that there are no name conflicts between both
# directory structures.  In technical speak, it makes sure that the set
# intersection of the two deep file hierarchies is zero..
def is_safe_pdir(pdir, tname):
    safe = True

    if os.path.exists(pdir):
        tdir = template_dir(tname)
        # Sanity check
        if not os.path.exists(tdir):
            print ("""
%(subcommand)s: project template directory could not be found.
%(subcommand)s: this should never happen!  please file a bug report.
%(subcommand0s: ignore any errors that follow.              
"""% ARGS).strip()
            safe = False

        tfiles = set(dir_walk(tdir))
        pfiles = set(dir_walk(pdir))
        isect = tfiles.intersection(pfiles)
        if len(isect)>0:
            ARGS["pdir"] = pdir
            ARGS["isect"] = ", ".join(list(isect))
            print ("""
%(subcommand)s: cowardly refusing to overwrite files in %(pdir)s.
%(subcommand)s: files which exist in both locations:
%(subcommand)s: %(isect)s
"""% ARGS).strip()
            safe = False

    return safe

##
# Command line processing.  The format of the command line for newproject is
# just complex enough to make this difficult to read, but also too simple to
# justify an external command line parser.
#
# See the docstring at the head of this file for a description of the command
# line structure of newproject.
def parse_args():
    fail = False

    if len(sys.argv) > 1:
        for opt in sys.argv[1:]:
            if opt[0] == '-':
                fail = True
                ARGS["opt"] = opt
                sys.argv.remove(opt)
                print ("""
%(subcommand)s: unrecognized option \'%(opt)s\'.
"""% ARGS).strip()

    if len(sys.argv) > 1:
        pname = sys.argv[1]
    else:
        pname = raw_input("Enter project name: ")

    if len(sys.argv) > 2:
        pdir = sys.argv[2]
    else:
        pdir = "-".join(["proj",pname])

    if not is_safe_pdir(pdir, "project"):
        fail = True
        ARGS["pdir"] = pdir
        print ("""
%(subcommand)s: \'%(pdir)s\' cannot be used as a project directory.
"""% ARGS).strip()

    if len(sys.argv) > 3:
        fail = True
        print ("""
%(subcommand)s: too many arguments (expected max. 2).
"""% ARGS).strip()

    if fail == True:
        print ("""
%(subcommand)s: try \'%(script)s help %(subcommand)s\' for more information.
"""% ARGS).strip(); sys.exit(-1)

    return pname, pdir

class Command(LabelCommand):
    option_list = LabelCommand.option_list + (
        make_option('-u', '--author',
                    action='store', dest='author',
                    default='Ada Lovelace',
                    help='Author\'s name.'),
        make_option('-m', '--email',
                    action='store', dest='email',
                    default='ada@westminster.ac.uk',
                    help='Author\'s primary email address.'),
    )
    help = "Creates a reusable Django project directory structure for the given project name in the current directory."
    args = "[projectname]"
    label = "project name"

    # Can't import settings during this command, because they haven't
    # necessarily been created.
    can_import_settings = False
    requires_model_validation = False
    output_transaction = False

    def handle_label(self, project_name, **options):
        print "testing"
        return "testing"
        import re
        import random
        import shutil

        pname, pdir = parse_args()
        tdir = template_dir("project")
        tfiles = set(dir_walk(tdir))

        res = [ (r"$PROJECT_NAME$", pname),
                (r"$PROJECT_NAME_DOUBLE_DASH$", "".zfill(len(pname)).replace("0","=")),
                (r"$AUTHOR_NAME$",  raw_input('Please enter author\'s name:  ')),
                (r"$AUTHOR_EMAIL$", raw_input('Please enter author\'s email: ')),
                (r"$SECRET_KEY$",   "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])),
              ]

        for tfile in tfiles:
            try:
                os.makedirs(os.path.dirname(os.path.join(pdir,tfile)))
            except:
                pass

            tfilename = os.path.join(tdir,tfile)
            pfilename = os.path.join(pdir,tfile)
            file = open(tfilename,"r")
            text = file.read()
            file.close()
            for (find, repl) in res:
                text = text.replace(find, repl)
            file = open(pfilename,"w")
            file.write(text)
            file.close()
            shutil.copymode(tfilename,pfilename)

##
# End of File
##
