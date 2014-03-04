'''
@author: Tommy
'''
import struct
dwPolynomial = 0x04C11DB7
def cal_crc(ptr):
    crc = 0xFFFFFFFF
    for i in ptr:
        xbit = 1 << 31
        data = i
        for bits in range(0, 32):
            if(crc & 0x80000000):
                crc <<= 1
                crc ^= dwPolynomial
            else:
                crc <<= 1
            if(data & xbit):
                crc ^= dwPolynomial
            xbit >>= 1
    my_crc = '%08x' %  (crc & 0xffffffff)
    return my_crc

def exp_data(data):
    all_len = len(data)
    #length is wrong
    if(all_len<11):
        print 'wrong length,unknown device!'
        return None
    r_sof0 = ord(data[0])
    r_sof1 = ord(data[1])    
    r_lenth = ord(data[2])
    r_did0 = ord(data[3])
    r_did1 = ord(data[4])
    r_did2 = ord(data[5])
    r_did3 = ord(data[6])
    r_did4 = ord(data[7])
    r_did5 = ord(data[8])
    r_did6 = ord(data[9])
    r_did7 = ord(data[10])
    r_cmd = ord(data[11])
    # r_data = []
    r_crc0 = '%02x' % ord(data[-4])
    r_crc1 = '%02x' % ord(data[-3])
    r_crc2 = '%02x' % ord(data[-2])
    r_crc3 = '%02x' % ord(data[-1])
    # crc 7F 7F 0a 11 22 33 44 55 66 77 88 10 01 FD 0E 3C 53
    lenth_data = all_len - 7 - 9
    my_crc = [r_lenth, r_did0, r_did1, r_did2, r_did3, r_did4, r_did5, r_did6, r_did7, r_cmd]
    for x in xrange(lenth_data):
        my_crc.append(ord(data[11 + x + 1]))
        # r_data.append(ord(data[11 + x + 1]))
    mycrc32 = cal_crc(my_crc)
    mycrc0 = mycrc32[0:2]
    mycrc1 = mycrc32[2:4]
    mycrc2 = mycrc32[4:6]
    mycrc3 = mycrc32[6:8]
    print 'crc0:',mycrc0,' ',mycrc1,' ',mycrc2,' ',mycrc3
    #======================match SOF===========================================
    #match 0x7f 0x7f #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if((r_sof0 != 0x7f) or (r_sof1 != 0x7f)):
        print 'wrong head'
        return ret_pack(data,0x0A,0x91,[0x02])
    #======================match length =======================================
    #match len #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if(r_lenth != all_len-7):
        print 'wrong lenth'
        return ret_pack(data,0x0A,0x91, [0x03])
    #======================match crc===========================================
    #match crc32 #match cmd=0x91 DATA[0]=0x01/0x02/0x03
    if (mycrc0 != r_crc0) or (mycrc1 != r_crc1) or (mycrc2 != r_crc2) or (mycrc3 != r_crc3):
        print 'wrong crc'
        return ret_pack(data,0x0A,0x91, [0x01])
    cmd = hex(cmd)
    #======================match cmd===========================================
    #match cmd=0x10
    if(cmd == '0x10'):
        is_install = ord(data[12])
        if is_install == 0x01:#already done
            print 'did is already online'
            return ret_pack(data, 0x09, 0x10) 
        elif is_install == 0x00:#first do,5*60s=0x01,0x2c
            print 'did is going to be online'
            return ret_pack(data, 0x0d, 0x10, [0x01,0x2c,0x01,0x2c])
    #match cmd=0x20 data=null len = 0x09
    elif(cmd == '0x20'):
        print 'did is sending data'
        #add to mysql by thread
        add_to_db(data)
        return ret_pack(data, 0x09, 0x20)
    #TODO update in real time
    elif(cmd == '0x21'):
        pass
    elif(cmd == '0x22'):
        pass

def ret_pack(raw_data,length,cmd,data=None):   
    did0 = ord(raw_data[3])
    did1 = ord(raw_data[4])
    did2 = ord(raw_data[5])
    did3 = ord(raw_data[6])
    did4 = ord(raw_data[7])
    did5 = ord(raw_data[8])
    did6 = ord(raw_data[9])
    did7 = ord(raw_data[10])
    my_crc = []
    if data == None:
        my_crc = ret_crc(raw_data,length,cmd)
    else:
        my_crc = ret_crc(raw_data,length,cmd,data)
    mycrc3 = my_crc[0]
    mycrc2 = my_crc[1]
    mycrc1 = my_crc[2]
    mycrc0 = my_crc[3]
    #TODO data chuli
    print 'crc1:',mycrc0,' ',mycrc1,' ',mycrc2,' ',mycrc3
    if data == None:
        return struct.pack('BBBBBBBBBBBBBBBB',0x7f,0x7f,length,did0,did1,did2,did3,did4,did5,did6,did7,cmd,mycrc0,mycrc1,mycrc2,mycrc3)
    else:
        if len(data) == 1:
            return struct.pack('BBBBBBBBBBBBBBBBB',0x7f,0x7f,length,did0,did1,did2,did3,did4,did5,did6,did7,cmd,data[0],mycrc0,mycrc1,mycrc2,mycrc3)
        elif len(data) == 4:#default setting for device
            return struct.pack('BBBBBBBBBBBBBBBBBBBB',0x7f,0x7f,length,did0,did1,did2,did3,did4,did5,did6,did7,cmd,data[0],data[1],data[2],data[3],mycrc0,mycrc1,mycrc2,mycrc3)


def ret_crc(raw_data,length,cmd,data=None):
    did0 = ord(raw_data[3])
    did1 = ord(raw_data[4])
    did2 = ord(raw_data[5])
    did3 = ord(raw_data[6])
    did4 = ord(raw_data[7])
    did5 = ord(raw_data[8])
    did6 = ord(raw_data[9])
    did7 = ord(raw_data[10])
    return_crc = [length, did0, did1, did2, did3, did4, did5, did6, did7, cmd]
    if data != None:
        for i in data:
            return_crc.append(i)
    rtncrc32 = cal_crc(return_crc)
    rtncrc3 = int(rtncrc32[0:2],16)
    rtncrc2 = int(rtncrc32[2:4],16)
    rtncrc1 = int(rtncrc32[4:6],16)
    rtncrc0 = int(rtncrc32[6:8],16)
    return [rtncrc3,rtncrc2,rtncrc1,rtncrc0]

def add_to_db(received_data):
    print received_data
    # ph1 = received_data[12:]
    # ph2 = 
    # turbidity1 =
    # turbidity2 = 
    # rc1 =
    # rc2 = 
    # do1 =
    # do2 = 
    # conductivity1 =
    # conductivity2 = 
    # fluoride1 =
    # fluoride2 = 
    # temperature1 =
    # temperature2 = 
    # d_hcl1 =
    # d_hcl2 = 
    # d_na2co31 =
    # d_na2co32 = 
    # d_h2so41 =
    # d_h2so42 = 
    # d_naoh1 =
    # d_naoh2 = 
    # orp1 =
    # orp2 = 
