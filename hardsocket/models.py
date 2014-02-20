from django.db import models

# Create your models here.
class Device(models.Model):
    d_id = models.CharField(max_length=50)
    d_info = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    status_id = models.CharField(max_length=2)
    period_mins = models.CharField(max_length=2)
    
    def __str__(self):
        return 'd_id:%s,d_info:%s,type_id:%s,status_id:%s,period_mins:%s' \
            % (self.d_id, self.d_info, self.type_id, self.status_id, self.period_mins)
    
class SendLog(models.Model):
    ph = models.CharField(max_length=10)
    send_time = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=50)
    def __str__(self):
        return 'ph:%s,send_time:%s,device_id:%s' % (self.ph,self.send_time,self.device_id)