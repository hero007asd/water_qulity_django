# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket.models import Water_param
from hardsocket.mymultiserver import openSocket,closeSocket
from django.http import HttpResponse
import json

#===================for Web====================================
def getAllCorpAvgInfo(request):
    print request.GET['city_id']
    obj ={'corp_info':[{'corp_id':'1','corp_name':'上海自来水有限公司','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'},{'corp_id':'2','corp_name':'上海市北自来水有限公司','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'}],'spot_info':[{'spot_id':'1','spot_status':'0','x_pos':'550','y_pos':'240'},{'spot_id':'2','spot_status':'1','x_pos':'500','y_pos':'200'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getCityReports(request):
    print request.GET['city_id']
    print request.GET['reports_type']
    obj = [{'city_name':'上海','city_ph':'6.9','city_conductivity':'1.2','city_DO':'4','city_rc':'0.4','city_turbidity':'0.8','city_temp':'30','time':'2014-03-04 16:24:23'},{'city_name':'上海','city_ph':'6.9','city_conductivity':'1.2','city_DO':'4','city_rc':'0.4','city_turbidity':'0.8','city_temp':'30','time':'2014-03-05 16:24:23'}]
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getOneSpotInfo(request):
    print request.GET['spot_id']
    obj = {'spot_id':'1','corp_name':'上海自来水公司','area_name':'浦东新区','spot_name':'XX检测点','spot_ph':'6.9','spot_conductivity':'1.2','spot_DO':'4','spot_rc':'0.4','spot_turbidity':'0.8','spot_temp':'30' ,'ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1','temp_status':'1'}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getOneCorpInfo(request):
    print request.GET['corp_id']
    obj = {'corp_info':[{'corp_name':'上海自来水公司','corpChild_name':'上海自来水公司一厂','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'},{'corp_name':'上海自来水公司','corpChild_name':'上海自来水公司一厂','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'}],'spot_info': [{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getOneCorpReports(request):
    print request.GET['corp_id']
    print request.GET['reports_type']
    obj = [{'corp_name':'自来水公司','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30','time':'2014-03-04 16:24:23'},{'corp_name':'自来水公司','corp_ph':'8.2','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30','time':'2014-03-05 16:24:23'}]
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getAreaAvgInfo(request):
    print request.GET['city_id']
    obj = {'area_info':[{'area_id':'1','areaName':'浦东新区','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'},{'area_id':'2','areaName':'闵行区','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'}],'spot_info':[{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'2','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)

def getOneAreaInfo(request):
    print request.GET['area_id']
    obj = {'area_info':[{'area_anme':'浦东新区','areaChild_name':'自来水一厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'},{'area_anme':'闵行区','areaChild_name':'自来水2厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'}],'spot_info': [{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'2','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    # return HttpResponse(results)
    c = request.GET['jsonpcallback']
    print 'jsonp:',c
    callback = '%s(%s)' % (c,obj)
    return HttpResponse(callback)