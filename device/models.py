from django.db import models as m

# Create your models here.

class Area(m.Model):
	area_name = m.CharField(max_length=20,blank=True,null=True)
	area_full = m.CharField(max_length=100,blank=True,null=True)
	parent_id = m.IntegerField()
	level_id = m.IntegerField()

class Watercorp(m.Model):
	corp_name=m.CharField(max_length=100,blank=True,null=True)
	area = m.ForeignKey(Area,blank=True,null=True)


class WaterSubCorp(m.Model):
	sub_corp_name = m.CharField(max_length=100,blank=True,null=True)
	corp = m.ForeignKey(Watercorp)

class Street(m.Model):
	street_name = m.CharField(max_length=100,blank=True,null=True)
	area = m.ForeignKey(Area)
	waterworks = m.ForeignKey(Watercorp)
		
class Device(m.Model):
	device_id = m.CharField(max_length=50)
	device_info = m.CharField(max_length=200,blank=True,null=True)
	area = m.ForeignKey(Area)
	street = m.ForeignKey(Street)
	corp = m.ForeignKey(Watercorp,blank=True,null=True)
	sub_corp = m.ForeignKey(WaterSubCorp,blank=True,null=True)
	type_id = m.IntegerField()
	status_id = m.IntegerField()
	Period_send = m.IntegerField()
	road_name = m.CharField(max_length=200,blank=True,null=True)
	# add by tommy 20140317
	x_pos = m.CharField(max_length=10,blank=True,null=True)
	y_pos = m.CharField(max_length=10,blank=True,null=True)

