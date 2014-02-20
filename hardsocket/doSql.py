'''
@author: William
'''
import MySQLdb
def insert_ph(ph,device_id):
    try:
        conn = MySQLdb.connect(host='192.168.20.113',user='root',passwd = 'honest1101',db='water_quanlity')
        cur = conn.cursor()
        sql = 'insert into hard_socket_sendlog(ph,send_time,device_id) values(%s,now(),%s)'
        param = (ph,device_id)
        count = cur.execute(sql,param)
        #if count<1 return 'please resend'
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
insert_ph('12', 'abbb')
