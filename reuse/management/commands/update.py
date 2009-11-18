#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.update
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
docstring for update.py
"""

from django.core.management.base import NoArgsCommand

import os
from subprocess import call

class Command(NoArgsCommand):
    help = "Updates git, svn, mtn, and hg repositoreis."

    requires_model_validation = False

    def handle_noargs(self, **options):
        dev_dir = os.path.abspath('.')
        for app_name in os.listdir(dev_dir):
            app_dir = os.path.abspath(os.path.join(dev_dir, app_name))
            if os.path.lexists(os.path.join(app_dir,'.svn')):
                print "Updating svn %s" % app_dir
                os.chdir(app_dir)
                call(['svn', 'update'])
            elif os.path.lexists(os.path.join(app_dir,'.git')):
                print "Updating git %s" % app_dir
                os.chdir(app_dir)
                call(['git', 'pull'])
            elif os.path.lexists(os.path.join(app_dir,'_MTN')):
                print "Updating mtn %s" % app_dir
                os.chdir(app_dir)
                call(['mtn', 'pull'])
                call(['mtn', 'update'])
            elif os.path.lexists(os.path.join(app_dir,'.hg')):
                print "Updating hg %s" % app_dir
                os.chdir(app_dir)
                call(['hg', 'pull'])
                call(['hg', 'update'])
            else:
                continue

##
# End of File
##
