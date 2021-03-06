#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.newproject
##

##
# Copyright (C) 2009, Mark Friedenbach <mark.friedenbach@nasa.gov>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of version 3 of the GNU Affero General Public License as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this source code; if not, see <http://www.gnu.org/licenses/>,
#   or write to
#
#     Free Software Foundation, Inc.
#     51 Franklin Street, Fifth Floor
#     Boston, MA  02110-1301  USA
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
from django.core.management.base import LabelCommand, CommandError
from optparse import make_option

import os
subcommand = os.path.basename(__file__)
subcommand = subcommand[:-len(".py")]
ARGS = { "subcommand": subcommand }

def dir_walk(dir):
    """
    dir_walk() takes a single directory as an argument and returns a list of
    all the files found by walking that directory hierarchy.  The relative
    paths of those files are included, but not the original directory.

    This function is used by is_safe_pdir() to see if there is any overlap
    between pdir (the user specified project directory) and tdir (the template
    directory which contains the skeleton project).
    """
    if not os.path.isdir(dir):
        return []
    
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

def template_dir():
    """
    template_dir() returns a path to the template directory in the
    django-reuse distribution.  It assumes that the template directory can be
    found relative to this source file.
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","..","..","templates")

def is_safe_pdir(pdir, tdir):
    """
    Checks that a directory is safe to use as the target of a directory copy
    operation.  Namely, it checks that the template directory exists, and that
    if the target directory exists that there are no name conflicts between
    both directory structures.  In technical speak, it makes sure that the set
    intersection of the two deep file hierarchies is zero..
    """
    safe = True

    if os.path.exists(pdir):
        # Sanity check
        if not os.path.exists(tdir):
            print ("""
%(subcommand)s: project template directory could not be found.
%(subcommand)s: this should never happen!  please file a bug report.
%(subcommand)s: ignore any errors that follow.              
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

class Command(LabelCommand):
    help = """
Creates a reusable Django project directory structure for the given project
name in the current directory.
""".strip()
    option_list = LabelCommand.option_list + (
        make_option('-u', '--author',
                    action='store', dest='author',
                    default='Ada Lovelace',
                    help="""
Author's name.
""".strip()),
        make_option('-m', '--email',
                    action='store', dest='email',
                    default='ada@westminster.ac.uk',
                    help="""
Author's primary email address.
""".strip()),
        make_option('-t', '--template',
                    action='store', dest='template',
                    default='basic',
                    help="""
Template to use.
""".strip()),
    )

    args = "[projectname]"
    label = "project name"

    can_import_settings = False
    requires_model_validation = False
    output_transaction = False

    def handle_label(self, pname, **options):
        import re
        import random
        import shutil
        import os
        import sys
        from subprocess import call
        
        basedir = os.path.join(os.path.dirname(__file__),'..','..','..','..')
        basedir = os.path.abspath(basedir)
        virtualdir = os.path.join(basedir,'.virtualenv',pname)
        if os.path.exists(virtualdir):
            ARGS["pname"]      = pname
            ARGS["virtualdir"] = virtualdir
            print ("""
%(subcommand)s: virtual environment '%(pname)s' already exists!
%(subcommand)s:
%(subcommand)s: %(subcommand)s is cowardly refusing to overwrite existing
%(subcommand)s: files.  please change your project name or remove these files
%(subcommand)s: before continuing.
"""% ARGS).strip()
            raise CommandError(("""
Virtual environment for '%(pname)s' already exists at '%(virtualdir)s'.
"""% ARGS).strip())
        
        pdir = "-".join(["proj",pname])
        tdir = os.path.join(template_dir(),"proj",options.get('template'))
        tfiles = set(dir_walk(tdir))
        
        if not is_safe_pdir(pdir,tdir):
            ARGS["pdir"] = pdir
            raise CommandError(("""
'%(pdir)s' cannot be used as a project directory.
"""% ARGS).strip())
        
        res = [ (r"$PROJECT_NAME$", pname),
                (r"$PROJECT_NAME_DOUBLE_DASH$", "".zfill(len(pname)).replace("0","=")),
                (r"$AUTHOR_NAME$",  options.get('author')),
                (r"$AUTHOR_EMAIL$", options.get('email')),
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
        
        # Create virtual environment
        virtualenv = os.path.join(basedir,'virtualenv','virtualenv.py')
        call([sys.executable,virtualenv,'--no-site-packages',virtualdir])
        
        # Link to source code within virtual environment
        os.symlink(os.path.join('..','..',pdir),
                   os.path.join(virtualdir,'proj'))
        
        # Fetch and install requirements
        call([os.path.join(virtualdir,'bin','python'),
              os.path.join(virtualdir,'bin','pip'),
              'install', '-r', os.path.join(pdir, 'requirements.txt')])

##
# End of File
##
