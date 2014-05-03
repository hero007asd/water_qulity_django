# -*- coding: UTF-8 -*-
from django.db import models as m
from device import models
from django.utils.html import format_html

#water_quality_log table     
class Water_param(m.Model):
    device = m.ForeignKey(models.Device,blank=True,null=True,verbose_name='设备')
    ph = m.CharField(max_length=20,blank=True,null=True,verbose_name='ph值')
    turbidity = m.CharField(max_length=20,blank=True,null=True,verbose_name='浊度值')
    rc = m.CharField(max_length=20,blank=True,null=True,verbose_name='余氯')
    d_oxygen = m.CharField(max_length=20,blank=True,null=True,verbose_name='溶解氧')
    conductivity = m.CharField(max_length=20,blank=True,null=True,verbose_name='电导率')
    fluoride = m.CharField(max_length=20,blank=True,null=True,verbose_name='氟离子')
    temperature = m.CharField(max_length=20,blank=True,null=True,verbose_name='温度')
    d_hcl = m.CharField(max_length=20,blank=True,null=True,verbose_name='hcl浓度')
    d_na2co3 = m.CharField(max_length=20,blank=True,null=True,verbose_name='na2co3浓度')
    d_h2so4 = m.CharField(max_length=20,blank=True,null=True,verbose_name='h2so4浓度')
    d_naoh = m.CharField(max_length=20,blank=True,null=True,verbose_name='naoh浓度')
    orp = m.CharField(max_length=20,blank=True,null=True,verbose_name='orp')
    is_ok = m.IntegerField(verbose_name='是否合格(0:不合格,1:合格)')
    send_time = m.DateTimeField(auto_now_add=True,verbose_name='接受时间')

    def send_time_fmt(self):
        return self.send_time.strftime('%Y-%m-%d %H:%M:%S')
    send_time_fmt.short_description = '接受时间'
    send_time_fmt.admin_order_field = 'send_time'

    def is_ok_fmt(self):
        if self.is_ok == 1:
            return format_html('<span style="color:green">正常</span>')
        else: return format_html('<span style="color:red">不正常</span>')
    is_ok_fmt.allow_tags = True
    is_ok_fmt.admin_order_field = 'is_ok'
    is_ok_fmt.short_description = '是否合格'


    def __str__(self):
        return 'device_id:%s,ph:%s,is_ok:%d' % (self.device_id, self.ph, self.is_ok)
    class Meta:
        verbose_name = '水质接受数据'    
        verbose_name_plural = '水质接受数据管理'


class Water_param_corp_week(m.Model):
    corp = m.ForeignKey(models.Watercorp)
    ph = m.CharField(max_length=20,blank=True,null=True)
    turbidity = m.CharField(max_length=20,blank=True,null=True)
    rc = m.CharField(max_length=20,blank=True,null=True)
    d_oxygen = m.CharField(max_length=20,blank=True,null=True)
    conductivity = m.CharField(max_length=20,blank=True,null=True)
    fluoride = m.CharField(max_length=20,blank=True,null=True)
    temperature = m.CharField(max_length=20,blank=True,null=True)
    d_hcl = m.CharField(max_length=20,blank=True,null=True)
    d_na2co3 = m.CharField(max_length=20,blank=True,null=True)
    d_h2so4 = m.CharField(max_length=20,blank=True,null=True)
    d_naoh = m.CharField(max_length=20,blank=True,null=True)
    orp = m.CharField(max_length=20,blank=True,null=True)
    is_ph_ok = m.IntegerField()
    is_turbidity_ok = m.IntegerField()
    is_rc_ok = m.IntegerField()
    is_do_ok = m.IntegerField()
    is_conductivity_ok = m.IntegerField()
    is_fluoride_ok = m.IntegerField()
    is_temperature_ok = m.IntegerField()
    is_hcl_ok = m.IntegerField()
    is_na2co3_ok = m.IntegerField()
    is_h2so4_ok = m.IntegerField()
    is_naoh_ok = m.IntegerField()
    is_orp_ok = m.IntegerField()
    is_ok = m.IntegerField()
    week_info = m.CharField(max_length=200,)#20140901-20140908,1st
    log_time = m.DateTimeField(auto_now_add=True)

class Water_param_corp_month(m.Model):
    corp = m.ForeignKey(models.Watercorp)
    ph = m.CharField(max_length=20,blank=True,null=True)
    turbidity = m.CharField(max_length=20,blank=True,null=True)
    rc = m.CharField(max_length=20,blank=True,null=True)
    d_oxygen = m.CharField(max_length=20,blank=True,null=True)
    conductivity = m.CharField(max_length=20,blank=True,null=True)
    fluoride = m.CharField(max_length=20,blank=True,null=True)
    temperature = m.CharField(max_length=20,blank=True,null=True)
    d_hcl = m.CharField(max_length=20,blank=True,null=True)
    d_na2co3 = m.CharField(max_length=20,blank=True,null=True)
    d_h2so4 = m.CharField(max_length=20,blank=True,null=True)
    d_naoh = m.CharField(max_length=20,blank=True,null=True)
    orp = m.CharField(max_length=20,blank=True,null=True)
    is_ph_ok = m.IntegerField()
    is_turbidity_ok = m.IntegerField()
    is_rc_ok = m.IntegerField()
    is_do_ok = m.IntegerField()
    is_conductivity_ok = m.IntegerField()
    is_fluoride_ok = m.IntegerField()
    is_temperature_ok = m.IntegerField()
    is_hcl_ok = m.IntegerField()
    is_na2co3_ok = m.IntegerField()
    is_h2so4_ok = m.IntegerField()
    is_naoh_ok = m.IntegerField()
    is_orp_ok = m.IntegerField()
    is_ok = m.IntegerField()
    month_info = m.CharField(max_length=200,)#20140901-20140908,1st
    log_time = m.DateTimeField(auto_now_add=True)

class Water_param_subcorp_week(m.Model):
    corp = m.ForeignKey(models.Watercorp)
    ph = m.CharField(max_length=20,blank=True,null=True)
    turbidity = m.CharField(max_length=20,blank=True,null=True)
    rc = m.CharField(max_length=20,blank=True,null=True)
    d_oxygen = m.CharField(max_length=20,blank=True,null=True)
    conductivity = m.CharField(max_length=20,blank=True,null=True)
    fluoride = m.CharField(max_length=20,blank=True,null=True)
    temperature = m.CharField(max_length=20,blank=True,null=True)
    d_hcl = m.CharField(max_length=20,blank=True,null=True)
    d_na2co3 = m.CharField(max_length=20,blank=True,null=True)
    d_h2so4 = m.CharField(max_length=20,blank=True,null=True)
    d_naoh = m.CharField(max_length=20,blank=True,null=True)
    orp = m.CharField(max_length=20,blank=True,null=True)
    is_ph_ok = m.IntegerField()
    is_turbidity_ok = m.IntegerField()
    is_rc_ok = m.IntegerField()
    is_do_ok = m.IntegerField()
    is_conductivity_ok = m.IntegerField()
    is_fluoride_ok = m.IntegerField()
    is_temperature_ok = m.IntegerField()
    is_hcl_ok = m.IntegerField()
    is_na2co3_ok = m.IntegerField()
    is_h2so4_ok = m.IntegerField()
    is_naoh_ok = m.IntegerField()
    is_orp_ok = m.IntegerField()
    is_ok = m.IntegerField()
    week_info = m.CharField(max_length=200,)#20140901-20140908,1st
    log_time = m.DateTimeField(auto_now_add=True)

class Water_param_subcorp_month(m.Model):
    corp = m.ForeignKey(models.Watercorp)
    ph = m.CharField(max_length=20,blank=True,null=True)
    turbidity = m.CharField(max_length=20,blank=True,null=True)
    rc = m.CharField(max_length=20,blank=True,null=True)
    d_oxygen = m.CharField(max_length=20,blank=True,null=True)
    conductivity = m.CharField(max_length=20,blank=True,null=True)
    fluoride = m.CharField(max_length=20,blank=True,null=True)
    temperature = m.CharField(max_length=20,blank=True,null=True)
    d_hcl = m.CharField(max_length=20,blank=True,null=True)
    d_na2co3 = m.CharField(max_length=20,blank=True,null=True)
    d_h2so4 = m.CharField(max_length=20,blank=True,null=True)
    d_naoh = m.CharField(max_length=20,blank=True,null=True)
    orp = m.CharField(max_length=20,blank=True,null=True)
    is_ph_ok = m.IntegerField()
    is_turbidity_ok = m.IntegerField()
    is_rc_ok = m.IntegerField()
    is_do_ok = m.IntegerField()
    is_conductivity_ok = m.IntegerField()
    is_fluoride_ok = m.IntegerField()
    is_temperature_ok = m.IntegerField()
    is_hcl_ok = m.IntegerField()
    is_na2co3_ok = m.IntegerField()
    is_h2so4_ok = m.IntegerField()
    is_naoh_ok = m.IntegerField()
    is_orp_ok = m.IntegerField()
    is_ok = m.IntegerField()
    month_info = m.CharField(max_length=200,)#20140901-20140908,1st
    log_time = m.DateTimeField(auto_now_add=True)