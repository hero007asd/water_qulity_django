from django.db import models as m

# Create your models here.

class Area(m.Model):
	area_name = m.CharField(max_length=20,blank=True,null=True)
	area_full = m.CharField(max_length=100,blank=True,null=True)
	parent_id = m.IntegerField()
	level_id = m.IntegerField()


class Watercorp(m.Model):
	corp_name=m.CharField(max_length=100,blank=True,null=True)
	parent_id = m.IntegerField()
	level_id = m.IntegerField()

class Waterworks(m.Model):
	w_name = m.CharField(max_length=100,blank=True,null=True)
	parent_id = m.IntegerField()
	level_id = m.IntegerField()
	corp_id = m.ForeignKey(Watercorp)



class Street(m.Model):
	street_name = m.CharField(max_length=100,blank=True,null=True)
	area_id = m.ForeignKey(Area)
	w_id = m.ForeignKey(Waterworks)
		
class Device(m.Model):
	device_info = m.CharField(max_length=200,blank=True,null=True)
	area_id = m.ForeignKey(Area)
	street_id = m.ForeignKey(Street)
	type_id = m.IntegerField()
	status_id = m.IntegerField()
	Period_send = m.IntegerField()