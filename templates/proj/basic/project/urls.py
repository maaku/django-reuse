#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# project.urls
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

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),
)

# Added by Mark Friedenbach 17 Jul 2009
# to support admin by configuration of settings.py
from django.conf import settings
if getattr(settings, 'ADMIN', False):
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
    ) + urlpatterns
    if getattr(settings, 'ADMIN_DOC', False):
        urlpatterns = patterns('',
            (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        ) + urlpatterns

# Added by Mark Friedenbach 15 Jul 2009
# to support media serving during development
from django.conf import settings
if getattr(settings, 'MEDIA_SERVE', False):
    urlpatterns = patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ) + urlpatterns

##
# End of File
##
