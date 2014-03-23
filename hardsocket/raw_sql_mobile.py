from django.db import connection

def __my_custome_sql(sql,*arg,**kword):
    cursor = connection.cursor()
    print '##$$$$arg:%s' % arg
    if arg:
        cursor.execute(sql,[a for a in arg])
        print '##%s,param:%s' % (sql,a)
    else:
        cursor.execute(sql)
    # row = cursor.fetchall()
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


#=============================================
def getCurOverView(street_name):
    sql = 'SELECT IFNULL(round(avg(b.ph),2),0) as cur_ph \
              ,IFNULL(round(avg(b.turbidity),2),0) as cur_turbidity \
              ,IFNULL(round(avg(b.conductivity),2),0) as cur_conductivity \
              ,IFNULL(round(avg(b.d_oxygen),2),0) as cur_DO \
              ,IFNULL(round(avg(b.rc),2),0) as cur_rc \
              ,d.corp_name as water_work_name \
              ,d.tel_no as water_work_phone \
            FROM device_device a \
            LEFT JOIN hardsocket_water_param b \
            ON a.id = b.device_id \
            AND TO_DAYS(b.send_time) = TO_DAYS(NOW()) \
            LEFT JOIN device_area c \
            ON a.area_id = c.id \
            LEFT JOIN device_watercorp d \
            ON a.corp_id = d.id \
            WHERE c.area_name = %s'
    return __my_custome_sql(sql,street_name)

#=============================================
def getOverView(city_name):
    sql = 'SELECT IFNULL(round(avg(c.ph),2),0) as ov_ph \
                ,IFNULL(round(avg(c.turbidity),2),0) as ov_turbidity \
                ,IFNULL(round(avg(c.conductivity),2),0) as ov_conductivity \
                ,IFNULL(round(avg(c.d_oxygen),2),0) as ov_DO \
                ,IFNULL(round(avg(c.rc),2),0) as ov_rc \
            FROM device_area a \
            LEFT JOIN device_device b \
            ON a.id = b.area_id  \
            LEFT JOIN hardsocket_water_param c \
            ON b.id = c.device_id \
            AND TO_DAYS(NOW()) =  TO_DAYS(c.send_time) \
            WHERE a.area_full LIKE %s'
    param = '%s%s%s'% ('%',city_name,'%')
    print '$$$city_name:%s' % city_name
    print '$$$param:%s' % param
    return __my_custome_sql(sql,param)


#=============================================


