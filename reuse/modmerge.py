#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: reuse.modmerge
##

##
# Copyright © by its contributors (see: COPYRIGHT.txt).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of version 3 of the GNU Affero General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this source code; if not, see <http://www.gnu.org/licenses/>
# or write to
#
#   Free Software Foundation, Inc.
#   51 Franklin Street, Fifth Floor
#   Boston, MA  02110-1301  USA
##

import os
import re
import types

def merge(package, dir):
    class_names = []
    for filename in os.listdir(dir):
        if not re.match(r"^.*.py$", filename) or filename == "__init__.py"
            continue
        module = __import__('%s.%s' % (package, filename[:-3]),
                            {}, {},
                            filename[:-3])
        for name in dir(module):
          item = getattr(module, name)
          if not isinstance(item, (type, types.ClassType)):
              continue
          exec "%s = item" % name
          class_names.append(name)
    return class_names

##
# End of File
##
