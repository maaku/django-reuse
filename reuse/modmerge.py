#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-reuse: reuse.modmerge
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
