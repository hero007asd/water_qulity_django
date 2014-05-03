# -*- coding: UTF-8 -*-
from django.db import models as m

# Create your models here.

class Area(m.Model):
	area_name = m.CharField(max_length=20,blank=True,null=True,verbose_name=u'区域名')
	area_full = m.CharField(max_length=100,blank=True,null=True,verbose_name=u'区域全名')
	parent_id = m.IntegerField()
	level_id = m.IntegerField(verbose_name=u'所属层级',)

	def __unicode__(self):
		return '%s' % (self.area_name,)
	class Meta:
		verbose_name = '区域'
		verbose_name_plural = '区域管理'


class Watercorp(m.Model):
	corp_name=m.CharField(max_length=100,blank=True,null=True,verbose_name=u'供水企业名')
	area = m.ForeignKey(Area,blank=True,null=True,verbose_name=u'所属区域')
	tel_no = m.CharField(max_length =100,blank=True,null=True,verbose_name=u'热线电话')

	def __unicode__(self):
		return '%s' % (self.corp_name,)
	class Meta:
		verbose_name = '供应水总公司'
		verbose_name_plural = '供应水总公司管理'


class WaterSubCorp(m.Model):
	sub_corp_name = m.CharField(max_length=100,blank=True,null=True,verbose_name=u'供水分公司名')
	corp = m.ForeignKey(Watercorp,verbose_name=u'所属公司企业')
	tel_no = m.CharField(max_length =100,blank=True,null=True,verbose_name=u'热线电话')

	def __unicode__(self):
		return '%s' % (self.sub_corp_name,)
	class Meta:
		verbose_name = '水分企业'
		verbose_name_plural = '水分企业管理'

class Street(m.Model):
	street_name = m.CharField(max_length=100,blank=True,null=True,verbose_name=u'街道名')
	area = m.ForeignKey(Area,verbose_name=u'所属区域')
	waterworks = m.ForeignKey(Watercorp,verbose_name=u'所属供水企业')

	def __unicode__(self):
		return '%s' % (self.street_name,)
	class Meta:
		verbose_name = '街道'
		verbose_name_plural = '街道管理'
		
class Device(m.Model):
	device_id = m.CharField(max_length=50)
	device_info = m.CharField(max_length=200,blank=True,null=True,verbose_name=u'设备名')
	area = m.ForeignKey(Area,blank=True,null=True,verbose_name=u'区域')
	street = m.ForeignKey(Street,blank=True,null=True,verbose_name=u'所属道路')
	corp = m.ForeignKey(Watercorp,blank=True,null=True,verbose_name=u'供水公司')
	sub_corp = m.ForeignKey(WaterSubCorp,blank=True,null=True,verbose_name=u'供水分公司')
	type_id = m.IntegerField(verbose_name=u'模块')
	status_id = m.IntegerField(verbose_name=u'状态')
	Period_send = m.IntegerField(blank=True,null=True,verbose_name=u'发送间隔(s)')
	period_collect = m.IntegerField(blank=True,null=True,verbose_name=u'采样间隔')
	road_name = m.CharField(max_length=200,blank=True,null=True,verbose_name=u'所在街道')
	# add by tommy 20140317
	x_pos = m.CharField(max_length=10,blank=True,null=True)
	y_pos = m.CharField(max_length=10,blank=True,null=True)

	def __unicode__(self):
		return '%s' % (self.device_info,)

	class Meta:
		# db_table = 'device_device'#数据库名字
		verbose_name = '设备'#修改从管理级 进入后的页面显示
		verbose_name_plural = '设备管理'


