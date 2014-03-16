'''
@author: Tommy
handle into db
'''
import struct
from hardsocket.models import Water_param
from device.models import Device
'''
insert into db with water's param
rec_data is a stream of data from socket
'''
def add_to_db(rec_data):
    device_id = struct.unpack('q',rec_data[3:11])[0]
    a = rec_data[12:-4]
    ph1 = struct.unpack('I',a[0:4][::-1])[0]
    ph2 = struct.unpack('B',a[4])[0]
    ph3 = struct.unpack('B',a[5])[0]
    turbidity1 = struct.unpack('I',a[6:10][::-1])[0]
    turbidity2 = struct.unpack('B',a[10])[0]
    turbidity3 = struct.unpack('B',a[11])[0]
    rc1 = struct.unpack('I',a[12:16][::-1])[0]
    rc2 = struct.unpack('B',a[16])[0]
    rc3 = struct.unpack('B',a[17])[0]
    do1 = struct.unpack('I',a[18:22][::-1])[0]
    do2 = struct.unpack('B',a[22])[0]
    do3 = struct.unpack('B',a[23])[0]
    conductivity1 = struct.unpack('I',a[24:28][::-1])[0]
    conductivity2 = struct.unpack('B',a[28])[0]
    conductivity3 = struct.unpack('B',a[29])[0] 
    fluoride1 = struct.unpack('I',a[30:34][::-1])[0]
    fluoride2 = struct.unpack('B',a[34])[0]
    fluoride3 = struct.unpack('B',a[35])[0]
    temperature1 = struct.unpack('I',a[36:40][::-1])[0]
    temperature2 = struct.unpack('B',a[40])[0]
    temperature3 = struct.unpack('B',a[41])[0]
    d_hcl1 = struct.unpack('I',a[42:46][::-1])[0]
    d_hcl2 = struct.unpack('B',a[46])[0]
    d_hcl3 = struct.unpack('B',a[47])[0]
    d_na2co31 = struct.unpack('I',a[48:52][::-1])[0]
    d_na2co32 = struct.unpack('B',a[52])[0]
    d_na2co33 = struct.unpack('B',a[53])[0]
    d_h2so41 = struct.unpack('I',a[54:58][::-1])[0]
    d_h2so42 = struct.unpack('B',a[58])[0]
    d_h2so43 = struct.unpack('B',a[59])[0]
    d_naoh1 = struct.unpack('I',a[60:64][::-1])[0]
    d_naoh2 = struct.unpack('B',a[64])[0]
    d_naoh3 = struct.unpack('B',a[65])[0]
    orp0 = struct.unpack('B',a[66])[0]
    orp1 = struct.unpack('BBB',a[67:70])
    orp2 = struct.unpack('B',a[70])[0]
    orp3 = struct.unpack('B',a[71])[0]
    #concreate value
    ph = '%s.%s%s' % (ph1,ph2,ph3)
    turbidity = '%s.%s%s' % (turbidity1,turbidity2,turbidity3)
    rc = '%s.%s%s' % (rc1,rc2,rc3)
    do_value = '%s.%s%s' % (do1,do2,do3)
    conductivity = '%s.%s%s' % (conductivity1,conductivity2,conductivity3)
    fluoride = '%s.%s%s' % (fluoride1,fluoride2,fluoride3)
    temperature = '%s.%s%s' % (temperature1,temperature2,temperature3)
    d_hcl = '%s.%s%s' % (d_hcl1,d_hcl2,d_hcl3)
    d_na2co3 = '%s.%s%s' % (d_na2co31,d_na2co32,d_na2co33)
    d_h2so4 = '%s.%s%s' % (d_h2so41,d_h2so42,d_h2so43)
    d_naoh = '%s.%s%s' % (d_naoh1,d_naoh2,d_naoh3)
    #solve for orp
    sign = ''
    if orp0 == 1:
        sign = '-'
    orp_integral = '%s%s%s' % (hex(orp1[0]).replace('0x',''),hex(orp1[1]).replace('0x',''),hex(orp1[2]).replace('0x',''))
    orp = '%s%d.%s%s' % (sign,int(orp_integral),orp2,orp3)
    # print 'ph:%s' % ph
    # print 'turbidity:%s' % turbidity
    # print 'rc:%s' % rc
    # print 'do_value:%s' % do_value
    # print 'conductivity:%s' % conductivity
    # print 'fluoride:%s' % fluoride
    # print 'temperature:%s' % temperature
    # print 'd_hcl:%s' % d_hcl
    # print 'd_na2co3:%s' % d_na2co3
    # print 'd_h2so4:%s' % d_h2so4
    # print 'd_naoh:%s' % d_naoh
    # print 'orp:%s' % orp
    # print 'device_ID:%s' % device_id
    # add to db
    device = Device.objects.get(device_id=device_id)
    if device:
        water_param = Water_param()
        water_param.device = device
        water_param.ph = ph
        water_param.turbidity = turbidity
        water_param.rc = rc 
        water_param.d_oxygen = do_value 
        water_param.conductivity = conductivity 
        water_param.fluoride = fluoride 
        water_param.temperature = temperature 
        water_param.d_hcl = d_hcl 
        water_param.d_na2co3 = d_na2co3 
        water_param.d_h2so4 = d_h2so4 
        water_param.d_naoh = d_naoh
        water_param.orp = orp
        water_param.is_ok = 0
        water_param.save()
