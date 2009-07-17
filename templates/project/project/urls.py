#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# project.urls
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
