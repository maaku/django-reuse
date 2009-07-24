#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# reuse.management.commands.hello
##

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Prints a hello, world! message."

    requires_model_validation = False

    def handle_noargs(self, **options):
        return "Hello, world!"

##
# End of File
##
