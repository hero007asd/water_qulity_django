'''
@author: Tommy
handle into db
'''
import struct
'''
insert into db with water's param
rec_data is a stream of data from socket
'''
def add_to_db(rec_data):
    a = rec_data[12:-4]
    ph1 = struct.unpack('I',a[0:4][::-1])[0]
    ph2 = struct.unpack('H',a[4:6][::-1])[0]
    turbidity1 = struct.unpack('I',a[6:10][::-1])[0]
    turbidity2 = struct.unpack('H',a[10:12][::-1])[0]
    rc1 = struct.unpack('I',a[12:16][::-1])[0]
    rc2 = struct.unpack('H',a[16:18][::-1])[0]
    do1 = struct.unpack('I',a[18:22][::-1])[0]
    do2 = struct.unpack('H',a[22:24][::-1])[0]
    conductivity1 = struct.unpack('I',a[24:28][::-1])[0]
    conductivity2 = struct.unpack('H',a[28:30][::-1])[0] 
    fluoride1 = struct.unpack('I',a[30:34][::-1])[0]
    fluoride2 = struct.unpack('H',a[34:36][::-1])[0]
    temperature1 = struct.unpack('I',a[36:40][::-1])[0]
    temperature2 = struct.unpack('H',a[40:42][::-1])[0]
    d_hcl1 = struct.unpack('I',a[42:46][::-1])[0]
    d_hcl2 = struct.unpack('H',a[46:48][::-1])[0]
    d_na2co31 = struct.unpack('I',a[48:52][::-1])[0]
    d_na2co32 = struct.unpack('H',a[52:54][::-1])[0]
    d_h2so41 = struct.unpack('I',a[54:58][::-1])[0]
    d_h2so42 = struct.unpack('H',a[58:60][::-1])[0]
    d_naoh1 = struct.unpack('I',a[60:64][::-1])[0]
    d_naoh2 = struct.unpack('H',a[64:66][::-1])[0]
    orp0 = struct.unpack('B',a[66:67][::-1])[0]
    orp1 = struct.unpack('BBB',a[67:70])
    orp2 = struct.unpack('H',a[70:72][::-1])[0]
    #concreate value
    ph = '%s.%s' % (ph1,ph2)
    turbidity = '%s.%s' % (turbidity1,turbidity2)
    rc = '%s.%s' % (rc1,rc2)
    do_value = '%s.%s' % (do1,do2)
    conductivity = '%s.%s' % (conductivity1,conductivity2)
    fluoride = '%s.%s' % (fluoride1,fluoride2)
    temperature = '%s.%s' % (temperature1,temperature2)
    d_hcl = '%s.%s' % (d_hcl1,d_hcl2)
    d_na2co3 = '%s.%s' % (d_na2co31,d_na2co32)
    d_h2so4 = '%s.%s' % (d_h2so41,d_h2so42)
    d_naoh = '%s.%s' % (d_naoh1,d_naoh2)
    #solve for orp
    sign = '+'
    if orp0 == 1:
        sign = '-'
    orp_integral = '%s%s%s' % (hex(orp1[0]).replace('0x',''),hex(orp1[1]).replace('0x',''),hex(orp1[2]).replace('0x',''))
    orp = '%s%d.%s' % (sign,int(orp_integral),orp2)
    print 'ph:%s' % ph
    print 'turbidity:%s' % turbidity
    print 'rc:%s' % rc
    print 'do_value:%s' % do_value
    print 'conductivity:%s' % conductivity
    print 'fluoride:%s' % fluoride
    print 'temperature:%s' % temperature
    print 'd_hcl:%s' % d_hcl
    print 'd_na2co3:%s' % d_na2co3
    print 'd_h2so4:%s' % d_h2so4
    print 'd_naoh:%s' % d_naoh
    print 'orp:%s' % orp
    # add to db