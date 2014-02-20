from django.shortcuts import render, render_to_response
from hardsocket.models import SendLog
from hardsocket.multiserverHex import manipulateSocket

def showPh(request):
    query = ''
    results = []
    if 'page' in request.GET:
        query = request.GET['page']
        if query is None:
            print 'query is none'
        else:
            print "query's page is %s" % query
            results = SendLog.objects.all()
    else:
        print 'query is ok'
        results = SendLog.objects.all()
        print results
    
    return render_to_response('show_ph.html',{'logs':results})

def manipulate(request):
    try:
        manipulateSocket()
    except Exception, e:
        raise e
    finally:
        print 'aaaa'

def socketAdmin(request):
    return render_to_response('hardsocket/socketAdmin.html')