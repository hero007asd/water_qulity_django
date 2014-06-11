'''
created by shitao.tommy
@datetime 20140412 23:48
@description insert into db with id
'''
import sys
sys.path.append('..\..')

from hardsocket import models
import device as _
def model_save(arrparam,did):
    medevice = _.models.Device.objects.get(device_id=did)
    if medevice:
        water_param = models.Water_param()
        water_param.device = medevice
        water_param.ph = arrparam[0]
        water_param.turbidity = arrparam[1]
        water_param.rc = arrparam[2]
        water_param.d_oxygen = arrparam[3]
        water_param.conductivity = arrparam[4]
        water_param.fluoride = arrparam[5]
        water_param.temperature = arrparam[6]
        water_param.d_hcl = arrparam[7]
        water_param.d_na2co3 = arrparam[8]
        water_param.d_h2so4 = arrparam[9]
        water_param.d_naoh =arrparam[10]
        water_param.orp =arrparam[11]
        ok_tag = 1 #ok
        if [i for i in arrparam if str(i).upper()=='FFFF']:
            ok_tag = 0
        water_param.is_ok = ok_tag
        water_param.save()
    else:
        pass

def getDeviceParam(did):
    medevice = _.models.Device.objects.get(device_id=did)
    if medevice:
        return medevice.Period_send,medevice.period_collect
    else:
        return None


