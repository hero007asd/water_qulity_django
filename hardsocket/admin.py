from django.contrib import admin
from hardsocket import models
# Register your models here.
class WaterParamAdmin(admin.ModelAdmin):
	list_display = ('device','ph','turbidity','rc','d_oxygen','conductivity','fluoride','temperature','d_hcl','d_na2co3','d_h2so4','d_naoh','orp','is_ok','send_time_fmt',)
	list_per_page = 20
    
admin.site.register(models.Water_param,WaterParamAdmin)