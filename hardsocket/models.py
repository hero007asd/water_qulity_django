from django.db import models as m
from device import models

# Create your models here.
# class Device(m.Model):
#     d_id = m.CharField(max_length=50)
#     d_info = m.CharField(max_length=50)
#     type_id = m.CharField(max_length=50)
#     status_id = m.CharField(max_length=2)
#     period_mins = m.CharField(max_length=2)
    
#     def __str__(self):
#         return 'd_id:%s,d_info:%s,type_id:%s,status_id:%s,period_mins:%s' 
#             % (self.d_id, self.d_info, self.type_id, self.status_id, self.period_mins)

#water_quality_log table     
class Water_param(m.Model):
    device_id = m.ForeignKey(models.Device,blank=True,null=True)
    ph = m.CharField(max_length=10,blank=True,null=True)
    turbidity = m.CharField(max_length=10,blank=True,null=True)
    conductivity = m.CharField(max_length=10,blank=True,null=True)
    d_oxygen = m.CharField(max_length=10,blank=True,null=True)
    residual_chlorine = m.CharField(max_length=10,blank=True,null=True)
    is_ok = m.IntegerField()
    send_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'device_id:%s,ph:%s,is_ok:%d' % (self.device_id, self.ph, self.is_ok)


