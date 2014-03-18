from django.contrib import admin
from device import models
# Register your models here.
admin.site.register(models.Device)
admin.site.register(models.Area)
admin.site.register(models.Street)
admin.site.register(models.Watercorp)
admin.site.register(models.WaterSubCorp)
