# -*- coding: UTF-8 -*-

# from django.test import TestCase
# from hardsocket import models
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# print BASE_DIR
# Create your tests here.
# a = models.Water_param()
# a.is_ok = 1
# a.save()
# str = '上海市浦东新区虚假弄路'
# # str.split('区')
# # print str.decode('utf-8')
# print str.split('区')[1]


# str = 'aaaa111'
# print str.startswith('aaaa2')

# a = ([1,2,3,4],['a','b','c','d'])
# b = ['one','two','three','four']
# print [dict(zip(b,i)) for i in a]

# if [i for i in b if i=='one' or i=='two']:
# 	print 'a'
# else:
# 	print 'b'

# lambda a : [a for i in b if i=='one' ]
from django.test import TestCase
from django.core.management import call_command
from hardsocket.gsmsocket import datahandle
class SimpleTest(TestCase):
    COMMON = ','
    def test_socket_insert(self):
        param = 'AT+00112233AABBCCDD,20,6.50,50.00,0.25,35.30,0.15,200.00,25.00,11.10,2.50,0.28,0.80,-508.00,\r\n'
        # call_command('gearman_submit_job','socket_insert',param)
        datahandle.handle_data(param)
