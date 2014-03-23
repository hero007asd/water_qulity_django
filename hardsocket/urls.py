# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from hardsocket import  views,viewsmobile,viewsweb,viewsweb_new
urlpatterns = patterns('',
    url(r'^manipulateSocket/$',views.manipulate,name='manipulateSocket'),
    url(r'^socketAdmin/$',TemplateView.as_view(template_name='hardsocket/socketAdmin.html'),name='socketAdmin'),
    url(r'^test_log/$',views.test_log),
    #for mobile 
    url(r'^showCurOverview/$',viewsmobile.showCurOverview),
    url(r'^showOverview/$',viewsmobile.showOverview),
    url(r'^showStreetValue/$',viewsmobile.showStreetValue),
    url(r'^showCurStreetValue/$',viewsmobile.showCurStreetValue),
    url(r'^getStreets/$',viewsmobile.getStreets),
    #for web
    url(r'^index/$',TemplateView.as_view(template_name='hardsocket/index.html'),name='index'),
    url(r'^aa/$',TemplateView.as_view(template_name='hardsocket/aa.html'),name='aa'),
    url(r'^pandect/$',TemplateView.as_view(template_name='hardsocket/pandect.html'),name='pandect'),
    url(r'^report/$',TemplateView.as_view(template_name='hardsocket/report.html'),name='report'),
    
    url(r'^getAllCorpAvgInfo/$',viewsweb_new.getAllCorpAvgInfo),
    url(r'^getAllCorpReports/$',viewsweb_new.getAllCorpReports),
    url(r'^getSubCorpReports/$',viewsweb_new.getSubCorpReports),
    url(r'^getCorpTrend/$',viewsweb_new.getCorpTrend),
    url(r'^getSubCorpTrend/$',viewsweb_new.getSubCorpTrend),

    url(r'^getOneSpotInfo/$',viewsweb_new.getOneSpotInfo),
    url(r'^getSpotDetailInfo/$',viewsweb_new.getSpotDetailInfo),
    
    url(r'^getOneCorpInfo/$',viewsweb_new.getOneCorpInfo),
    url(r'^getAreaAvgInfo/$',viewsweb_new.getAreaAvgInfo),
    url(r'^getOneAreaInfo/$',viewsweb_new.getSubAreaInfo),
)