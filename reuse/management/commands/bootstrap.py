#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.bootstrap
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
Usage: bootstrap [directory]

Builds an environment for developing reusable Django applications and projects
in the directory specified, including downloading updated releases of Django
and the most common tools and applications.
"""

##
# Boilerplate
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

import os
subcommand = os.path.basename(__file__)
subcommand = subcommand[:-len(".py")]
ARGS = { "subcommand": subcommand }

##
# Ideally this should be derived from LabelCommand, but LabelCommand currently
# provides no capability for default labels.  This functionality should be in
# Django core, and a ticket (#11590) has been generated:
#   <http://code.djangoproject.com/ticket/11590>
class Command(BaseCommand):
    help = """
Builds an environment for developing reusable Django applications and projects
in the directory specified, including downloading updated releases of Django
and the most common tools and applications.
""".strip()

    args = "[directory]"
    label = "directory"

    can_import_settings = False
    requires_model_validation = False
    output_transaction = False

    def handle(self, *labels, **options):
        if not labels:
            # This next line is the only difference from LabelCommand.  If
            # only there were an easier way to override this behavior...
            labels = [os.getcwd()]

        output = []
        for label in labels:
            label_output = self.handle_label(label, **options)
            if label_output:
                output.append(label_output)
        return '\n'.join(output)

    def handle_label(self, label, **options):
        pass

##
# End of File
##
