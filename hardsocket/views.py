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
def showCity(request):
    obj = {'ph':1,'do':2}
    results = json.dumps(obj)

    return HttpResponse(results)