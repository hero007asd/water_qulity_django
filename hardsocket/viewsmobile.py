# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket.models import Water_param
from hardsocket.mymultiserver import openSocket,closeSocket
from django.http import HttpResponse
from hardsocket import raw_sql_mobile
import json
#===================for mobile===============================

'''
# TODO fix the range of some params of the water
'''
def showCurOverview(request):
    address = None
    if 'address' in request.POST:
        address = request.POST['address']
    elif 'address' in request.GET:
        address = request.GET['address']
    obj = raw_sql_mobile.getCurOverView(address)
    cur = obj[0]
    obj[0]['cur_status'] = 1
    if int(cur['cur_ph']) >6 and int(cur['cur_ph']) < 8:
        obj[0]['ph_status'] = 1
    else: 
        obj[0]['ph_status'] = 0
        obj[0]['cur_status'] = 0

    if int(cur['cur_turbidity']) >6 and int(cur['cur_turbidity']) < 8:
        obj[0]['turbidity_status'] = 1
    else: 
        obj[0]['turbidity_status'] = 0
        obj[0]['cur_status'] = 1

    if int(cur['cur_DO']) >6 and int(cur['cur_DO']) < 8:
        obj[0]['do_status'] = 1
    else :
        obj[0]['do_status'] = 0
        obj[0]['cur_status'] = 1

    if int(cur['cur_rc']) >6 and int(cur['cur_rc']) < 8:
        obj[0]['rc_status'] = 1
    else :
        obj[0]['rc_status'] = 0
        obj[0]['cur_status'] = 1

    if int(cur['cur_conductivity']) >6 and int(cur['cur_conductivity']) < 8:
        obj[0]['conductivity_status'] = 1
    else :
        obj[0]['conductivity_status'] = 0
        obj[0]['cur_status'] = 1
    results = json.dumps(obj[0],ensure_ascii=False)

    return HttpResponse(results)

'''
# TODO fix the range of some params of the water
'''
def showOverview(request):
    param = None
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    city = param['city']
    obj = raw_sql_mobile.getOverView(city)
    cur = obj[0]
    obj[0]['ov_status'] = 1
    if int(cur['ov_ph']) >6 and int(cur['ov_ph']) < 8:
        obj[0]['ph_status'] = 1
    else: 
        obj[0]['ph_status'] = 0
        obj[0]['ov_status'] = 0

    if int(cur['ov_turbidity']) >6 and int(cur['ov_turbidity']) < 8:
        obj[0]['turbidity_status'] = 1
    else: 
        obj[0]['turbidity_status'] = 0
        obj[0]['ov_status'] = 1

    if int(cur['ov_DO']) >6 and int(cur['ov_DO']) < 8:
        obj[0]['do_status'] = 1
    else :
        obj[0]['do_status'] = 0
        obj[0]['ov_status'] = 1

    if int(cur['ov_rc']) >6 and int(cur['ov_rc']) < 8:
        obj[0]['rc_status'] = 1
    else :
        obj[0]['rc_status'] = 0
        obj[0]['ov_status'] = 1

    if int(cur['ov_conductivity']) >6 and int(cur['ov_conductivity']) < 8:
        obj[0]['conductivity_status'] = 1
    else :
        obj[0]['conductivity_status'] = 0
        obj[0]['ov_status'] = 1
    # obj = {'ov_ph':'6.9','ov_turbidity':'0.8','ov_conductivity':'1.2','ov_DO':'4','ov_rc':'0.4','ov_status':'1','ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1'}
    results = json.dumps(obj[0],ensure_ascii=False)
    return HttpResponse(results)

def showStreetValue(request):
    param = None
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    value_type = param['value_type']
    area_id = param['area_id']
    street_id = param['street_id']
    #TODO
    results = __foo(value_type,area_id,street_id,1)
    return HttpResponse(results)

def showCurStreetValue(request):
    param = None
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    value_type = param['value_type']
    area_name = param['area_name']
    street_name = param['street_name']
    #TODO
    results = __foo(value_type,area_name,street_name,2)
    return HttpResponse(results)

def getStreets(request):
    print request.GET
    print request.POST
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    area_id = param['area_id']
    #TODO use area_id get streets
    # obj = [{'street_id':'20001','street_name':'七宝镇'},{'street_id':'20002','street_name':'龙柏街道'},{'street_id':'20003','street_name':'九亭镇'},]
    obj = raw_sql_mobile.getStreetsSql(area_id)
    results = json.dumps(obj,ensure_ascii=False)
    return HttpResponse(results)


def __phJson(area_id,street_id,id_or_name):
    if id_or_name == 1:
        obj = {'type':'1','value':raw_sql_mobile.getStreetValue('1',street_id),'avgValue':raw_sql_mobile.getStreetAvgValue('1',street_id)}
    else:
        obj = {'type':'1','value':raw_sql_mobile.getCurStreetValue('1',street_id),'avgValue':raw_sql_mobile.getCurStreetAvgValue('1',street_id)}
    return json.dumps(obj)

def __turbidityJson(area_id,street_id,id_or_name):
    if id_or_name == 1:    
        obj = {'type':'2','value':raw_sql_mobile.getStreetValue('2',street_id),'avgValue':raw_sql_mobile.getStreetAvgValue('2',street_id)}
    else:    
        obj = {'type':'2','value':raw_sql_mobile.getCurStreetValue('2',street_id),'avgValue':raw_sql_mobile.getCurStreetAvgValue('2',street_id)}

    return json.dumps(obj)

def __conductivityJson(area_id,street_id,id_or_name):
    if id_or_name == 1:
        obj = {'type':'3','value':raw_sql_mobile.getStreetValue('3',street_id),'avgValue':raw_sql_mobile.getStreetAvgValue('3',street_id)}
    else:
        obj = {'type':'3','value':raw_sql_mobile.getCurStreetValue('3',street_id),'avgValue':raw_sql_mobile.getCurStreetAvgValue('3',street_id)}

    return json.dumps(obj)

def __doJson(area_id,street_id,id_or_name):
    if id_or_name == 1:
        obj = {'type':'4','value':raw_sql_mobile.getStreetValue('4',street_id),'avgValue':raw_sql_mobile.getStreetAvgValue('4',street_id)}
    else:
        obj = {'type':'4','value':raw_sql_mobile.getCurStreetValue('4',street_id),'avgValue':raw_sql_mobile.getCurStreetAvgValue('4',street_id)}

    return json.dumps(obj)

def __rcJson(area_id,street_id,id_or_name):
    if id_or_name == 1:
        obj = {'type':'5','value':raw_sql_mobile.getStreetValue('5',street_id),'avgValue':raw_sql_mobile.getStreetAvgValue('5',street_id)}
    else:
        obj = {'type':'5','value':raw_sql_mobile.getCurStreetValue('5',street_id),'avgValue':raw_sql_mobile.getCurStreetAvgValue('5',street_id)}

    return json.dumps(obj)

operator = {'1':__phJson,'2':__turbidityJson,'3':__conductivityJson,'4':__doJson,'5':__rcJson}

def __foo(bar,area_id,street_id,id_or_name):
    if callable(operator.get(bar)):
        return operator.get(bar)(area_id,street_id,id_or_name)
    else:
        return None
    