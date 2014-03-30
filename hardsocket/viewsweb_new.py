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

def getCorpTrend(request):
    city_id = request.GET['city_id']
    reports_type = request.GET['reports_type']
    obj = None
    if reports_type == '1':
        obj = raw_sql.getCorpDayTrend(city_id)
    elif reprots_type == '2':
        obj = raw_sql.getCorpWeekTrend(city_id)
    elif reprots_type == '3':
        obj = raw_sql.getCorpMonthTrend(city_id)
    
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getSubCorpTrend(request):
    corp_id = request.GET['corp_id']
    reports_type = request.GET['reports_type']
    obj = None
    if reports_type == '1':
        obj = raw_sql.getSubCorpDayTrend(corp_id)
    elif reprots_type == '2':
        obj = raw_sql.getSubCorpWeekTrend(corp_id)
    elif reprots_type == '3':
        obj = raw_sql.getSubCorpMonthTrend(corp_id)

    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneSpotInfo(request):
    spot_id = request.GET['spot_id']
    obj = raw_sql.getOneSpotInfo(spot_id)
    obj[0]['last_time'] = str(obj[0]['last_time'])
    results = json.dumps(obj[0],ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getSpotDetailInfo(request):
    spot_id = request.GET['spot_id']
    obj = raw_sql.getSpotDetailInfo(spot_id)
    for i in obj:
        i['last_time'] = str(i['last_time'])
    obj = {'spot_id':obj[0]['spot_id'],'corp_name':obj[0]['corp_name'],'area_name':obj[0]['area_name'],'spot_name':obj[0]['spot_name'],'spt_detail':obj}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getOneCorpInfo(request):
    corp_id = request.GET['corp_id']
    spotInfo = raw_sql.getOneSpotInfo(corp_id)
    for i in spotInfo:
        i['last_time'] = str(i['last_time'])
    obj = {'corp_info':spotInfo,'spot_info': raw_sql.getCorpSpotInfo(corp_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)


def getAreaAvgInfo(request):
    city_id = request.GET['city_id']
    obj = {'area_info':raw_sql.getAreaAvgInfo(city_id),'spot_info':raw_sql.getAreaSpotInfo(city_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)

def getSubAreaInfo(request):
    area_id = request.GET['area_id']
    obj = {'area_info':[{'area_anme':'浦东新区','areaChild_name':'自来水一厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'},{'area_anme':'闵行区','areaChild_name':'自来水2厂','area_ph':'6.9','area_conductivity':'1.2','area_DO':'4','area_rc':'0.4','area_turbidity':'0.8','area_temp':'30'}],'spot_info': raw_sql.getSubAreaSpotInfo(area_id)}
    results = json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return HttpResponse(results)