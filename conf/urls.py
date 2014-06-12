# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hardsocket/', include('hardsocket.urls',namespace='hardsocket')),
    ('^site_media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATICFILES_DIRS[1]}),
)
