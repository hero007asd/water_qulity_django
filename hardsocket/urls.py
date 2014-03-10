from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from hardsocket import  views,viewsmobile,viewsweb
urlpatterns = patterns('',
    url(r'^index/$',views.showPh,name='showPH'),
    url(r'^manipulateSocket/$',views.manipulate,name='manipulateSocket'),
    url(r'^socketAdmin/$',TemplateView.as_view(template_name='hardsocket/socketAdmin.html'),name='socketAdmin'),
    #for mobile 
    url(r'^showCurOverview/$',viewsmobile.showCurOverview),
    url(r'^showOverview/$',viewsmobile.showOverview),
    url(r'^showStreetValue/$',viewsmobile.showStreetValue),
    url(r'^showCurStreetValue/$',viewsmobile.showCurStreetValue),
    url(r'^getStreets/$',viewsmobile.getStreets),
    #for web
    url(r'^getAllCorpAvgInfo/$',viewsweb.getAllCorpAvgInfo),
    url(r'^getCityReports/$',viewsweb.getCityReports),
    url(r'^getOneSpotInfo/$',viewsweb.getOneSpotInfo),
    url(r'^getOneCorpInfo/$',viewsweb.getOneCorpInfo),
    url(r'^getOneCorpReports/$',viewsweb.getOneCorpReports),
    url(r'^getAreaAvgInfo/$',viewsweb.getAreaAvgInfo),
    url(r'^getOneAreaInfo/$',viewsweb.getOneAreaInfo),
)