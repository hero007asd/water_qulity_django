from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from hardsocket import  views
urlpatterns = patterns('',
    url(r'^index/$',views.showPh,name='showPH'),
    url(r'^manipulateSocket/$',views.manipulate,name='manipulateSocket'),
    url(r'^socketAdmin/$',TemplateView.as_view(template_name='hardsocket/socketAdmin.html'),name='socketAdmin'),
    url(r'^showCityForMobile/$',views.showCity),
)