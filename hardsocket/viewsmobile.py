# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket.models import Water_param
from hardsocket.mymultiserver import openSocket,closeSocket
from django.http import HttpResponse
import json
#===================for mobile====================================
def showCurOverview(request):
    print request.GET 
    print request.POST 
    address = None
    obj = {'cur_ph':'6.9','cur_turbidity':'0.8','cur_conductivity':'1.2','cur_DO':'4','cur_rc':'0.4','cur_status':'1','ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1','water_work_name':'上海市北水厂临港镇分公司','water_work_phone':'021-65748901'}
    results = json.dumps(obj,ensure_ascii=False)

    return HttpResponse(results)

def showOverview(request):
    # print request.GET 
    # print request.POST 
    obj = {'ov_ph':'6.9','ov_turbidity':'0.8','ov_conductivity':'1.2','ov_DO':'4','ov_rc':'0.4','ov_status':'1','ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1'}
    results = json.dumps(obj)

    return HttpResponse(results)

def showStreetValue(request):
    param = None
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    value_type = param['value_type']
    #TODO
    results = __foo(value_type)
    return HttpResponse(results)

def showCurStreetValue(request):
    param = None
    if('info' in request.POST):
        param = json.loads(request.POST['info'])
    elif('info' in request.GET):
        param = json.loads(request.GET['info'])
    value_type = param['value_type']
    #TODO
    results = __foo(value_type)
    return HttpResponse(results)

def getStreets(request):
    print request.GET
    print request.POST
    area_id = None
    if('area_id' in request.POST):
        area_id = request.POST['area_id']
    elif('area_id' in request.GET):
        area_id = request.GET['area_id']
    #TODO use area_id get streets
    obj = [{'street_id':'20001','street_name':'七宝镇'},{'street_id':'20002','street_name':'龙柏街道'},{'street_id':'20003','street_name':'九亭镇'},]
    results = json.dumps(obj,ensure_ascii=False)
    return HttpResponse(results)


def __phJson():
    obj = {'type':'1','value':[{'ph':'5.6','time':'1'},{'ph':'7','time':'2'},{'ph':'8','time':'3'},{'ph':'7.2','time':'4'},{'ph':'9','time':'5'},{'ph':'5.7','time':'6'},{'ph':'8','time':'7'},{'ph':'5.7','time':'8'},{'ph':'5.7','time':'9'},{'ph':'6.0','time':'10'},{'ph':'7.0','time':'11'},{'ph':'5.7','time':'12'},{'ph':'5.7','time':'13'},{'ph':'5.7','time':'14'},{'ph':'5.7','time':'15'},{'ph':'5.7','time':'16'},{'ph':'12.0','time':'17'},{'ph':'5.0','time':'18'},{'ph':'5.7','time':'19'},{'ph':'5.7','time':'20'},{'ph':'6.9','time':'21'},{'ph':'5.7','time':'22'},{'ph':'5.7','time':'23'},{'ph':'5.7','time':'24'}]}
    return json.dumps(obj)
def __turbidityJson():
    obj = {'type':'2','value':[{'turbidity':'5.6','time':'1'},{'turbidity':'5.7','time':'2'}]}
    return json.dumps(obj)
def __conductivityJson():
    obj = {'type':'3','value':[{'conductivity':'5.6','time':'1'},{'conductivity':'5.7','time':'2'}]}
    return json.dumps(obj)
def __doJson():
    obj = {'type':'4','value':[{'DO':'5.6','time':'1'},{'DO':'5.7','time':'2'}]}
    return json.dumps(obj)
def __rcJson():
    obj = {'type':'5','value':[{'rc':'5.6','time':'1'},{'rc':'5.7','time':'2'}]}
    return json.dumps(obj)
operator = {'1':__phJson,'2':__turbidityJson,'3':__conductivityJson,'4':__doJson,'5':__rcJson}
def __foo(bar):
    if callable(operator.get(bar)):
        return operator.get(bar)()
    else:
        return None
    