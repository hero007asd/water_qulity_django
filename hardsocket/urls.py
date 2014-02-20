from django.conf.urls import patterns, url
from hardsocket import  views
urlpatterns = patterns('',
    url(r'^index/$',views.showPh,name='showPH'),
    url(r'^manipulateSocket/$',views.manipulate,name='manipulateSocket'),
    url(r'^socketAdmin/$',views.socketAdmin,name='socketAdmin'),
)