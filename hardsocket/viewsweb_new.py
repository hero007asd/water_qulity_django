# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket import raw_sql
from hardsocket.mymultiserver import openSocket,closeSocket
from django.http import HttpResponse
import json

#===================for Web====================================
def getAllCorpAvgInfo(request):
    city_id = request.GET['city_id']

    obj = {'corp_info':raw_sql.getAllCorpAvgInfo(city_id),'spot_info':raw_sql.getAllSpot(city_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getAllCorpReports(request):
    city_id = request.GET['city_id']
    print request.GET['city_id']
    obj = {'todayInfo':raw_sql.getCorpTodayReports(city_id),'weekInfo':raw_sql.getCorpWeekReports(city_id),'MonthInfo':raw_sql.getCorpMonthReports(city_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getSubCorpReports(request):
    corp_id = request.GET['corp_id']
    print request.GET['corp_id']
    obj = {'todayInfo':raw_sql.getSubCorpTodayReports(corp_id),'weekInfo':raw_sql.getSubCorpWeekReports(corp_id),'MonthInfo':raw_sql.getSubCorpMonthReports(corp_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneSpotInfo(request):
    print request.GET['spot_id']
    obj = {'spot_id':'1','corp_name':'上海自来水公司','area_name':'浦东新区','spot_name':'XX检测点','spot_ph':'6.9','spot_conductivity':'1.2','spot_DO':'4','spot_rc':'0.4','spot_turbidity':'0.8','spot_temp':'30' ,'ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1','temp_status':'1'}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneCorpInfo(request):
    print request.GET['corp_id']
    obj = {'corp_info':[{'corp_name':'上海自来水公司','corpChild_name':'上海自来水公司一厂','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'},{'corp_name':'上海自来水公司','corpChild_name':'上海自来水公司一厂','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30'}],'spot_info': [{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneCorpReports(request):
    print request.GET['corp_id']
    print request.GET['reports_type']
    obj = [{'corp_name':'自来水公司','corp_ph':'6.9','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30','time':'2014-03-04 16:24:23'},{'corp_name':'自来水公司','corp_ph':'8.2','corp_conductivity':'1.2','corp_DO':'4','corp_rc':'0.4','corp_turbidity':'0.8','corp_temp':'30','time':'2014-03-05 16:24:23'}]
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getAreaAvgInfo(request):
    print request.GET['city_id']
    obj = {'area_info':[{'area_id':'1','areaName':'浦东新区','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'},{'area_id':'2','areaName':'闵行区','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'}],'spot_info':[{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'2','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneAreaInfo(request):
    print request.GET['area_id']
    obj = {'area_info':[{'area_anme':'浦东新区','areaChild_name':'自来水一厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'},{'area_anme':'闵行区','areaChild_name':'自来水2厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'}],'spot_info': [{'spot_id':'1','spot_status':'1','x_pos':'123','y_pos':'240'},{'spot_id':'2','spot_status':'1','x_pos':'123','y_pos':'220'}]}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)