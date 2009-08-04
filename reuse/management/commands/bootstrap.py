#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.bootstrap
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
