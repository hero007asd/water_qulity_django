# -*- coding: UTF-8 -*-
from django.db import connection
'''
add sql's log: and hardsocket_water_param.is_ok =1 
20140413
'''
def __my_custome_sql(sql,*arg,**kword):
    cursor = connection.cursor()
    if arg:
        cursor.execute(sql,[a for a in arg])
    else:
        cursor.execute(sql)
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


#=============================================
def getCurOverView(street_name):
    sql = 'SELECT IFNULL(round(b.ph,2),0) as cur_ph \
              ,IFNULL(round(b.turbidity,2),0) as cur_turbidity \
              ,IFNULL(round(b.conductivity,2),0) as cur_conductivity \
              ,IFNULL(round(b.d_oxygen,2),0) as cur_DO \
              ,IFNULL(round(b.rc,2),0) as cur_rc \
              ,IFNULL(round(b.orp,2),0) as cur_orp \
              ,IFNULL(CONCAT(d.corp_name,",",e.sub_corp_name),"暂未提供") as water_work_name \
              ,IFNULL(d.tel_no,"暂未提供") as water_work_phone \
            FROM device_device a \
            LEFT JOIN hardsocket_water_param b \
            ON a.id = b.device_id \
            AND TO_DAYS(b.send_time) = TO_DAYS(NOW()) \
            LEFT JOIN device_street f \
            ON a.street_id = f.id \
            LEFT JOIN device_watercorp d \
            ON a.corp_id = d.id \
            LEFT JOIN device_watersubcorp e \
            ON a.sub_corp_id = e.id \
            WHERE f.street_name LIKE %s \
            ORDER BY b.send_time desc LIMIT 1'
    param = '%s%s%s'% ('%',street_name,'%')
    return __my_custome_sql(sql,param)

#=============================================
def getStreetOverView(street_id):
    sql = 'SELECT IFNULL(round(avg(b.ph),2),0) as cur_ph \
              ,IFNULL(round(avg(b.turbidity),2),0) as cur_turbidity \
              ,IFNULL(round(avg(b.conductivity),2),0) as cur_conductivity \
              ,IFNULL(round(avg(b.d_oxygen),2),0) as cur_DO \
              ,IFNULL(round(avg(b.rc),2),0) as cur_rc \
              ,IFNULL(round(avg(b.orp),2),0) as cur_orp \
              ,IFNULL(CONCAT(d.corp_name,",",e.sub_corp_name),"暂未提供") as water_work_name \
              ,IFNULL(d.tel_no,"暂未提供") as water_work_phone \
            FROM device_device a \
            LEFT JOIN hardsocket_water_param b \
            ON a.id = b.device_id \
            AND TO_DAYS(b.send_time) = TO_DAYS(NOW()) \
            LEFT JOIN device_street c \
            ON a.street_id = c.id \
            LEFT JOIN device_watercorp d \
            ON a.corp_id = d.id \
            LEFT JOIN device_watersubcorp e \
            ON a.sub_corp_id = e.id \
            WHERE c.id = %s'
    return __my_custome_sql(sql,street_id)

#=============================================
def getOverView(city_name):
    sql = 'SELECT IFNULL(round(avg(c.ph),2),0) as ov_ph \
                ,IFNULL(round(avg(c.turbidity),2),0) as ov_turbidity \
                ,IFNULL(round(avg(c.conductivity),2),0) as ov_conductivity \
                ,IFNULL(round(avg(c.d_oxygen),2),0) as ov_DO \
                ,IFNULL(round(avg(c.rc),2),0) as ov_rc \
                ,IFNULL(round(avg(c.orp),2),0) as ov_orp \
            FROM device_area a \
            LEFT JOIN device_device b \
            ON a.id = b.area_id  \
            LEFT JOIN hardsocket_water_param c \
            ON b.id = c.device_id \
            AND TO_DAYS(NOW()) =  TO_DAYS(c.send_time) \
            WHERE a.area_full LIKE %s'
    param = '%s%s%s'% ('%',city_name,'%')
    return __my_custome_sql(sql,param)


#=============================================
def getStreetValue(type_value,street_id):
    pre_sql = __pre_sql(type_value)
    sql = pre_sql+',hour(a.send_time) as time \
        from hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_street c \
        ON b.street_id = c.id \
        WHERE day(NOW()) = day(a.send_time) \
        AND c.id = %s \
        GROUP BY c.id,time'
    return __my_custome_sql(sql,street_id)

#====================增加orp选项=========================
def __pre_ph_sql():
    return 'SELECT IFNULL(round(AVG(a.ph),2),0) as ph'

def __pre_turbidity_sql():
    return 'SELECT IFNULL(round(AVG(a.turbidity),2),0) as turbidity'

def __pre_conductivity_sql():
    return 'SELECT IFNULL(round(AVG(a.conductivity),2),0) as conductivity'

def __pre_do_sql():
    return 'SELECT IFNULL(round(AVG(a.d_oxygen),2),0) as DO'

def __pre_rc_sql():
    return 'SELECT IFNULL(round(AVG(a.rc),2),0) as rc'
def __pre_orp_sql():
    return 'SELECT IFNULL(round(AVG(a.orp),2),0) as orp'

operator = {'1':__pre_ph_sql,'2':__pre_turbidity_sql,'3':__pre_conductivity_sql,'4':__pre_do_sql,'5':__pre_rc_sql,'6':__pre_orp_sql}

def __pre_sql(type_value):
    if callable(operator.get(type_value)):
        return operator.get(type_value)()
    else:
        return None


#=============================================
def getCurStreetValue(type_value,street_name):
    pre_sql = __pre_sql(type_value)
    sql = pre_sql+',hour(a.send_time) as time \
        from hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_street c \
        ON b.street_id = c.id \
        WHERE day(NOW()) = day(a.send_time) \
        AND c.street_name LIKE %s \
        GROUP BY c.id,time'
    param = '%s%s%s'% ('%',street_name,'%')
    return __my_custome_sql(sql,param)


def getStreetsSql(area_id):
    sql = 'SELECT a.id as street_id \
            ,a.street_name as street_name \
            FROM device_street a \
            WHERE a.area_id = %s'
    return __my_custome_sql(sql,area_id)

def getStreetAvgValue(type_value,street_id):
    pre_sql = __pre_sql(type_value)
    sql = pre_sql+' from hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_street c \
        ON b.street_id = c.id \
        WHERE day(NOW()) = day(a.send_time) \
        AND c.id = %s'
    return __my_custome_sql(sql,street_id)

def getCurStreetAvgValue(type_value,street_name):
    pre_sql = __pre_sql(type_value)
    sql = pre_sql+' from hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_street c \
        ON b.street_id = c.id \
        WHERE day(NOW()) = day(a.send_time) \
        AND c.street_name LIKE %s  '
    param = '%s%s%s'% ('%',street_name,'%')
    return __my_custome_sql(sql,param)