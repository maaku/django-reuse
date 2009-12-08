#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# manage.py
##

##
# Copyright (C) $YEAR$, $AUTHOR_NAME$ <$AUTHOR_EMAIL$>
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

if __name__ == "__main__":

 ##
 # Added by Mark Friedenbach 28 Jul 2009
 #
 # Add the project directory and module to the python path.
 import os
 import sys
 import subprocess
 DIRNAME = os.path.dirname(os.path.abspath(__file__))
 sys.path.insert(0, DIRNAME)
 sys.path.insert(0, os.path.join(DIRNAME, 'apps'))
 sys.path.insert(0, os.path.join(DIRNAME, 'project'))

 ##
 # Added by Mark Friedenbach 28 Jul 2009
 #
 # We'll search all directories in the absolute and real paths, in that order,
 # until we find a django-reuse directory that contains a bin/manage.py, which
 # we'll execute with the same parameters that were passed to us.

 def unwind_path(path):
     if len(path) < 1 or path == os.sep:
         return [path]
     else:
         return [path] + unwind_path(os.path.dirname(path))

 dirs =        unwind_path(os.path.dirname(sys.argv[0]))
 dirs = dirs + unwind_path(os.path.abspath(DIRNAME))
 dirs = dirs + unwind_path(os.path.realpath(DIRNAME))

 # Remove duplicates (and empties), but keep original order
 temp = list(set(dirs))
 temp.remove('')
 temp.sort(cmp=lambda x,y: cmp(dirs.index(x), dirs.index(y)))
 dirs = temp

 # Now go through directory list looking for django-reuse or just reuse.
 path = ""
 for dir in dirs:
     file = os.path.join(dir, "django-reuse", "bin", "manage.py")
     if not os.path.isfile(file):
         file = os.path.join(dir, "reuse", "..", "bin", "manage.py")
         if not os.path.isfile(file):
             continue
     envs = os.environ
     envs['PYTHONPATH'] = ":".join(sys.path)
     theproc = subprocess.Popen([sys.executable, file] + sys.argv[1:], cwd=DIRNAME, env=envs)
     theproc.communicate()
     sys.exit(0)

 sys.stderr.write("""
error: Could not find django-reuse installation.  Are you sure that your
error: development environment is setup correctly?
""".lstrip())
 sys.exit(1)

##
# End of File
##
