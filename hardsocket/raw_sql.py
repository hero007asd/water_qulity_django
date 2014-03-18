from django.db import connection

def __my_custome_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    # row = cursor.fetchall()
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
#=============================================
def getAllCorpAvgInfo(city_id):
    sql = 'SELECT a.id as corp_id,a.corp_name as corp_name,\
        avg(c.ph) as corp_ph,\
        avg(c.conductivity) as corp_conductivity,\
        avg(c.d_oxygen) as corp_DO,\
        avg(c.rc) as corp_rc,\
        avg(c.turbidity) as corp_turbidity,\
        avg(c.temperature) as corp_temp \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON c.device_id = b.id \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        AND d.parent_id = 310000 \
        GROUP BY b.corp_id'
    return __my_custome_sql(sql)

def getAllSpot(city_id):
    sql = 'SELECT a.id,a.status_id as spot_status,a.x_pos,a.y_pos FROM device_device a \
        LEFT JOIN device_area b \
        ON a.area_id = b.id \
        WHERE b.parent_id = 310000'
    return __my_custome_sql(sql)

#=============================================
import datetime
today = datetime.datetime.now()
timespan = today.weekday()
def getFirstdayOfWeek():
    return firstday = datetime.datetime.now()-datetime.timedelta(days=int(timespan))
def getLastdayOfWeek():
    return getFirstdayOfWeek()+datetime.timedelta(days=6)

def getCorpTodayReports(city_id):
    sql = 'SELECT a.id as corp_id,a.corp_name as corp_name,\
        avg(c.ph) as corp_ph,\
        avg(c.conductivity) as corp_conductivity,\
        avg(c.d_oxygen) as corp_DO,\
        avg(c.rc) as corp_rc,\
        avg(c.turbidity) as corp_turbidity,\
        avg(c.temperature) as corp_temp \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON c.device_id = b.id \
        AND TO_DAYS(c.send_time) = TO_DAYS(now()) \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        AND d.parent_id = 310000 \
        GROUP BY b.corp_id'
    return __my_custome_sql(sql)

def getCorpWeekReports(city_id):
    sql = 'SELECT a.id as corp_id,a.corp_name as corp_name,\
        avg(c.ph) as corp_ph,\
        avg(c.conductivity) as corp_conductivity,\
        avg(c.d_oxygen) as corp_DO,\
        avg(c.rc) as corp_rc,\
        avg(c.turbidity) as corp_turbidity,\
        avg(c.temperature) as corp_temp \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON c.device_id = b.id \
        AND TO_DAYS(c.send_time) = TO_DAYS(now()) \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        AND d.parent_id = 310000 \
        GROUP BY b.corp_id'
    return __my_custome_sql(sql)

#=============================================



#=============================================



#=============================================



#=============================================
