import os 
os.environ['DJANGO_SETTINGS_MODULE'] = 'water_qulity_django.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
