# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket.models import Water_param
from hardsocket.multiserverHex import openSocket,closeSocket
from django.http import HttpResponse
import json
#====================About socket ============================================
def manipulate(request):
    #TODO 500 happened if add the threading?
    openSocket()

def close(request):
    closeSocket()

#======================client show ==================================================
# def socketAdmin(request):
#     return render_to_response('hardsocket/socketAdmin.html')


def showPh(request):
    query = ''
    results = []
    # if 'page' in request.GET:
    #     query = request.GET['page']
    #     if query is None:
    #         print 'query is none'
    #     else:
    #         print "query's page is %s" % query
    #         results = SendLog.objects.all()
    # else:
    results = Water_param.objects.order_by('-send_time')

    return render_to_response('hardsocket/show_ph.html',{'water':results})

#===================for web==============================



#===================for mobile====================================
def showCurOverview(request):
    print request.GET 
    print request.POST 
    obj = {'cur_ph':'6.9','cur_turbidity':'0.8','cur_conductivity':'1.2','cur_DO':'4','cur_rc':'0.4','cur_status':'1','ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1','water_work_name':'上海市北水厂临港镇分公司','water_work_phone':'021-65748901'}
    results = json.dumps(obj,ensure_ascii=False)

    return HttpResponse(results)

def showOverview(request):
    print request.GET 
    print request.POST 
    obj = {'ov_ph':'6.9','ov_turbidity':'0.8','ov_conductivity':'1.2','ov_DO':'4','ov_rc':'0.4','ov_status':'1','ph_status':'1','turbidity_status':'1','conductivity_status':'1','do_status':'1','rc_status':'1'}
    results = json.dumps(obj)

    return HttpResponse(results)

def showStreetValue(request):
    print request.GET 
    print request.POST
    value_type = None
    if('value_type' in request.POST):
        value_type = request.POST['value_type']
    elif('value_type' in request.GET):
        value_type = request.GET['value_type']
    results = __foo(value_type)

    return HttpResponse(results)

def showCurStreetValue(request):
    print request.GET 
    print request.POST
    value_type = None
    if('value_type' in request.POST):
        value_type = request.POST['value_type']
    elif('value_type' in request.GET):
        value_type = request.GET['value_type']
    results = __foo(value_type)

    return HttpResponse(results)


def __phJson():
    obj = {'type':'1','value':[{'ph':'5.6','time':'00:00'},{'ph':'5.7','time':'01:00'}]}
    return json.dumps(obj)
def __turbidityJson():
    obj = {'type':'2','value':[{'turbidity':'5.6','time':'00:00'},{'turbidity':'5.7','time':'01:00'}]}
    return json.dumps(obj)
def __conductivityJson():
    obj = {'type':'3','value':[{'conductivity':'5.6','time':'00:00'},{'conductivity':'5.7','time':'01:00'}]}
    return json.dumps(obj)
def __doJson():
    obj = {'type':'4','value':[{'DO':'5.6','time':'00:00'},{'DO':'5.7','time':'01:00'}]}
    return json.dumps(obj)
def __rcJson():
    obj = {'type':'5','value':[{'rc':'5.6','time':'00:00'},{'rc':'5.7','time':'01:00'}]}
    return json.dumps(obj)
operator = {'1':__phJson,'2':__turbidityJson,'3':__conductivityJson,'4':__doJson,'5':__rcJson}
def __foo(bar):
    if callable(operator.get(bar)):
        return operator.get(bar)()
    else:
        return None
    