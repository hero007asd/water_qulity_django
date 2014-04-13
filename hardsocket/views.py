# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from hardsocket import mymultiserver
from hardsocket.gsmsocket import gsmsocketserver
from django.http import HttpResponse
import json
import logging
#====================About socket ============================================
def openGsmSocket(request):
    try:
        gsmsocketserver.openSocket()
    except Exception, e:
        return HttpResponse('open socket is already open')
    return HttpResponse('open socket success')


def openWifiSocket(request):
    try:
        mymultiserver.openSocket()
    except Exception, e:
        return HttpResponse('open socket is already open')
    return HttpResponse('open socket success')

def closeWifiSocket(request):
    mymultiserver.closeSocket()

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

def test_log(request):
    log = logging.getLogger('socket.crc')
    log.error('wrong happened!!!')
    return HttpResponse('a')