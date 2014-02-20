from django.db import models as m

# Create your models here.
class Device(m.Model):
    d_id = m.CharField(max_length=50)
    d_info = m.CharField(max_length=50)
    type_id = m.CharField(max_length=50)
    status_id = m.CharField(max_length=2)
    period_mins = m.CharField(max_length=2)
    
    def __str__(self):
        return 'd_id:%s,d_info:%s,type_id:%s,status_id:%s,period_mins:%s' \
            % (self.d_id, self.d_info, self.type_id, self.status_id, self.period_mins)
    
class SendLog(m.Model):
    ph = m.CharField(max_length=10)
    send_time = m.DateTimeField(auto_now_add=True)
    device_id = m.CharField(max_length=50)
    def __str__(self):
        return 'ph:%s,send_time:%s,device_id:%s' % (self.ph,self.send_time,self.device_id)

class Water_param(m.Model):
    device_id = m.ForeignKey(Device,blank=True,null=True)
    ph_value = m.CharField(max_length=10)
    value_1 = m.CharField(max_length=10,blank=True,null=True)
    send_time = m.DateTimeField(auto_now_add=True)


