from django.contrib import admin
from device import models
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_info','area','street','corp','sub_corp','type_id','status_id','road_name','Period_send')
    #fields = ('device_info','area','street')

class StreetAdmin(admin.ModelAdmin):
    list_display = ('street_name','area','waterworks')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('area_name','area_full','level_id')

class WaterSubCorpAdmin(admin.ModelAdmin):
    list_display = ('sub_corp_name','corp','tel_no')

class WatercorpAdmin(admin.ModelAdmin):
    list_display = ('corp_name','area','tel_no')

admin.site.register(models.Device,DeviceAdmin)
admin.site.register(models.Area,AreaAdmin)
admin.site.register(models.Street,StreetAdmin)
admin.site.register(models.Watercorp,WatercorpAdmin)
admin.site.register(models.WaterSubCorp,WaterSubCorpAdmin)
