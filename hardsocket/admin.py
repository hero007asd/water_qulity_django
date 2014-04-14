from django.contrib import admin
from hardsocket import models
# from myapp.widgets import RichTextEditorWidget
# Register your models here.
class WaterParamAdmin(admin.ModelAdmin):
	list_display = ('device','ph','turbidity','rc','d_oxygen','conductivity','fluoride','temperature','d_hcl','d_na2co3','d_h2so4','d_naoh','orp','is_ok_fmt','send_time_fmt',)
	list_per_page = 20
	list_filter = ('is_ok','send_time','device__device_info')
	fieldsets = (
		(None,{
			'fields':('device','ph','turbidity','rc','d_oxygen','conductivity','fluoride','temperature','d_hcl','d_na2co3','d_h2so4','d_naoh','orp','is_ok',),
			# 'description':('aaaa')
			}),
	    )	
	# formfield_overrides = {
	# 	models.TextField: {'widget':RichTextEditorWidget},
	# }
    
admin.site.register(models.Water_param,WaterParamAdmin)