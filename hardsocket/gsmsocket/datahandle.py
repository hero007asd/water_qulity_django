# -*- coding: UTF-8 -*-
'''
created by tommy_shi
@date 2014-04-12
@time 21:55
@desc handle socket with ascii's text
'''
import socketsql

COMMON = ','
starttag = 'AT+'
endtag = '\r\n'

def handle_data(data):
    if data and len(data.split(COMMON)) < 3:
		raise ValueError('receive data,error happend')
    if not data.startswith(starttag):
        raise ValueError('wrong start tag')
    if not data.endswith(endtag):
    	raise ValueError('wrong end tag')

    arr = data.split(COMMON,2)
    did = arr[0][3:]

    # if len(did) != 16:
    # 	raise ValueError('device id length is wrong')

    rtArr = []
    if arr[1] == '10':
		rtArr = __get10MD(arr[2],did)
		if rtArr is None: 
			raise ValueError('receive cmd=10 data,error happend') 
    elif arr[1] == '20':
		rtArr = __get20MD(arr[2],did)
		if rtArr is None: 
			raise ValueError('receive cmd=20 data,error happend') 
    elif arr[1] == '21':
		rtArr = __get21MD(arr[2])
		if rtArr is None: 
			raise ValueError('receive cmd=21 data,error happend') 

    rtArr.insert(0,arr[0])
    rtArr.insert(1,arr[1])
    rtArr.append(endtag)
    return COMMON.join(rtArr)

def __get10MD(data,did,cmd='0',toservertime='300',collecttime='1'):
    rtArr = []
    myarr = data.split(COMMON)
    if len(myarr) != 2:return None
    config = myarr[0]

    if config == '0':#unconfiged
        #get period from db
        c = socketsql.getDeviceParam(did)
        if c:
            (toservertime,collecttime) = c
        rtArr.extend([cmd,str(toservertime),str(collecttime)])
    elif config == '1':#already configed
        rtArr.append(cmd)
    return rtArr

def __get20MD(data,did,cmd='0'):#0:nothing 1:to update 2:to get rightnow
    rtarr = []
    myarr = data.split(COMMON)
    if len(myarr) != 13: return None
    #insert into db
    socketsql.model_save(myarr,did)

    rtarr.append(cmd)
    return rtarr

def __get21MD(data,cmd='0'):
    rtarr = []
    myarr = data.split(COMMON)
    if len(myarr) > 13 or len(myarr) < 1: return None
    rtarr.append(cmd)
    # TODO handle
    return rtarr

if __name__ == '__main__':
	pass
    # handle_data('ahandle_data')
	# handle_data('AT+00112233AABBCCDD,20,6.50,50.00,0.25,35.30,0.15,200.00,25.00,11.10,2.50,0.28,0.80,-508.00,\\r\\n')
	# handle_data('AT+00112233AABBCCDD,10,0,\\r\\n')
	# handle_data('AT+00112233AABBCCDD,10,1,\\r\\n')
	# handle_data('AT+00112233AABBCCDD,21,1,1,0,0,\\r\\n')