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

a = ([1,2,3,4],['a','b','c','d'])
b = ['one','two','three','four']
print [dict(zip(b,i)) for i in a]

if [i for i in b if i=='one' or i=='two']:
	print 'a'
else:
	print 'b'

lambda a : [a for i in b if i=='one' ]

