from django.db import connection

def __my_custome_sql(sql,*arg,**kword):
    cursor = connection.cursor()
    if arg:
        cursor.execute(sql,[a for a in arg])
    else:
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
import calendar as cal
today = datetime.datetime.now()
timespan = today.weekday()
year = today.timetuple().tm_year
month = today.timetuple().tm_mon
def getFirstdayOfWeek():
    return datetime.datetime.now()-datetime.timedelta(days=int(timespan))
def getLastdayOfWeek():
    return getFirstdayOfWeek()+datetime.timedelta(days=6)
def getFirstdayOfMonth():
    return '%s-%s-%s' % (year,month,'1')
def getLastdayOfMonth():
    return '%s-%s-%s' % (year,month,cal.monthrange(year, month)[1])

def getCorpTodayReports(city_id):
    sql = 'SELECT a.id as corp_id,a.corp_name as corp_name,\
        avg(c.ph) as day_ph,\
        avg(c.conductivity) as day_conductivity,\
        avg(c.d_oxygen) as day_DO,\
        avg(c.rc) as day_rc,\
        avg(c.turbidity) as day_turbidity,\
        avg(c.temperature) as day_temp \
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
        avg(c.ph) as week_ph,\
        avg(c.conductivity) as week_conductivity,\
        avg(c.d_oxygen) as week_DO,\
        avg(c.rc) as week_rc,\
        avg(c.turbidity) as week_turbidity,\
        avg(c.temperature) as week_temp \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON c.device_id = b.id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) <= TO_DAYS(%s) \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        AND d.parent_id = 310000 \
        GROUP BY b.corp_id'
    return __my_custome_sql(sql,getFirstdayOfWeek(),getLastdayOfWeek())

def getCorpMonthReports(city_id):
    sql = 'SELECT a.id as corp_id,a.corp_name as corp_name,\
        avg(c.ph) as month_ph,\
        avg(c.conductivity) as month_conductivity,\
        avg(c.d_oxygen) as month_DO,\
        avg(c.rc) as month_rc,\
        avg(c.turbidity) as month_turbidity,\
        avg(c.temperature) as month_temp \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON c.device_id = b.id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) <= TO_DAYS(%s) \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        AND d.parent_id = 310000 \
        GROUP BY b.corp_id'
    return __my_custome_sql(sql,getFirstdayOfMonth(),getLastdayOfMonth())
#=============================================
def getSubCorpTodayReports(corp_id):
    sql = 'SELECT d.id as corp_id,d.sub_corp_name as corp_name,\
        avg(c.ph) as week_ph, \
        avg(c.conductivity) as week_conductivity, \
        avg(c.d_oxygen) as week_DO, \
        avg(c.rc) as week_rc, \
        avg(c.turbidity) as week_turbidity, \
        avg(c.temperature) as week_temp  \
        FROM device_watersubcorp d \
        LEFT JOIN device_watercorp a \
        ON d.corp_id = a.id \
        LEFT JOIN device_device b  \
        ON a.id = b.corp_id \
        AND d.id = b.sub_corp_id \
        LEFT JOIN hardsocket_water_param c  \
        ON c.device_id = b.id  \
        AND TO_DAYS(c.send_time) = TO_DAYS(now())  \
        WHERE a.id = 2 \
        GROUP BY d.id'
    return __my_custome_sql(sql)

def getSubCorpWeekReports(corp_id):
    sql = 'SELECT d.id as corp_id,d.sub_corp_name as corp_name,\
        avg(c.ph) as week_ph, \
        avg(c.conductivity) as week_conductivity, \
        avg(c.d_oxygen) as week_DO, \
        avg(c.rc) as week_rc, \
        avg(c.turbidity) as week_turbidity, \
        avg(c.temperature) as week_temp  \
        FROM device_watersubcorp d \
        LEFT JOIN device_watercorp a \
        ON d.corp_id = a.id \
        LEFT JOIN device_device b  \
        ON a.id = b.corp_id \
        AND d.id = b.sub_corp_id \
        LEFT JOIN hardsocket_water_param c  \
        ON c.device_id = b.id  \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) <= TO_DAYS(%s) \
        WHERE a.id = 2 \
        GROUP BY d.id'
    return __my_custome_sql(sql,getFirstdayOfWeek(),getLastdayOfWeek())

def getSubCorpMonthReports(corp_id):
    sql = 'SELECT d.id as corp_id,d.sub_corp_name as corp_name,\
        avg(c.ph) as week_ph, \
        avg(c.conductivity) as week_conductivity, \
        avg(c.d_oxygen) as week_DO, \
        avg(c.rc) as week_rc, \
        avg(c.turbidity) as week_turbidity, \
        avg(c.temperature) as week_temp  \
        FROM device_watersubcorp d \
        LEFT JOIN device_watercorp a \
        ON d.corp_id = a.id \
        LEFT JOIN device_device b  \
        ON a.id = b.corp_id \
        AND d.id = b.sub_corp_id \
        LEFT JOIN hardsocket_water_param c  \
        ON c.device_id = b.id  \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) <= TO_DAYS(%s) \
        WHERE a.id = 2 \
        GROUP BY d.id'
    return __my_custome_sql(sql,getFirstdayOfMonth(),getLastdayOfMonth())


#=============================================
def getCorpDayTrend(city_id):
    sql = 'SELECT a.id\
        ,a.corp_name\
        ,avg(c.ph) as corp_ph\
        ,avg(c.conductivity) as corp_conductivity\
        ,avg(c.d_oxygen) as corp_DO\
        ,avg(c.rc) as corp_rc \
        ,avg(c.turbidity) as corp_turbidity \
        ,avg(c.temperature) as corp_temp \
        ,HOUR(c.send_time) as time \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON b.id = c.device_id \
        AND TO_DAYS(c.send_time) = TO_DAYS(now()) \
        LEFT JOIN device_area d \
        ON a.area_id = d.id  \
        AND d.parent_id = %s \
        GROUP BY a.id,time'
    return __my_custome_sql(sql,city_id)

def getCorpWeekTrend(city_id):
    sql = 'SELECT a.id\
        ,a.corp_name\
        ,avg(c.ph) as corp_ph\
        ,avg(c.conductivity) as corp_conductivity\
        ,avg(c.d_oxygen) as corp_DO\
        ,avg(c.rc) as corp_rc \
        ,avg(c.turbidity) as corp_turbidity \
        ,avg(c.temperature) as corp_temp \
        ,WEEKDAY(c.send_time)+1 as time \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON b.id = c.device_id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        LEFT JOIN device_area d \
        ON a.area_id = d.id  \
        AND d.parent_id = %s \
        GROUP BY a.id,time'
    return __my_custome_sql(sql,getFirstdayOfWeek(),getLastdayOfWeek(),city_id)

def getCorpMonthTrend(city_id):
    sql = 'SELECT a.id\
        ,a.corp_name\
        ,avg(c.ph) as corp_ph\
        ,avg(c.conductivity) as corp_conductivity\
        ,avg(c.d_oxygen) as corp_DO\
        ,avg(c.rc) as corp_rc \
        ,avg(c.turbidity) as corp_turbidity \
        ,avg(c.temperature) as corp_temp \
        ,day(c.send_time) as time \
        FROM device_watercorp a \
        LEFT JOIN device_device b \
        ON a.id = b.corp_id \
        LEFT JOIN hardsocket_water_param c \
        ON b.id = c.device_id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        LEFT JOIN device_area d \
        ON a.area_id = d.id  \
        AND d.parent_id = %s \
        GROUP BY a.id,time'
    return __my_custome_sql(sql,getFirstdayOfMonth(),getLastdayOfMonth(),city_id)

#=============================================
def getSubCorpDayTrend(corp_id):
    sql='SELECT a.id \
        ,a.sub_corp_name \
        ,avg(d.ph) as corp_ph \
        ,avg(d.conductivity) as corp_conductivity \
        ,avg(d.d_oxygen) as corp_DO \
        ,avg(d.rc) as corp_rc \
        ,avg(d.turbidity) as corp_turbidity \
        ,avg(d.temperature) as corp_temp \
        ,hour(d.send_time) as time \
        FROM device_watersubcorp a \
        LEFT JOIN device_watercorp b \
        ON a.corp_id = b.id \
        LEFT JOIN device_device c \
        ON a.id = c.sub_corp_id \
        LEFT JOIN hardsocket_water_param d \
        ON c.id = d.device_id \
        AND TO_DAYS(d.send_time) = TO_DAYS(now()) \
        LEFT JOIN device_area e \
        ON e.id = c.area_id \
        WHERE a.corp_id = %s \
        GROUP BY a.id,time \
        ORDER BY a.id'
    return __my_custome_sql(sql,getFirstdayOfWeek(),getLastdayOfWeek(),corp_id)

def getSubCorpWeekTrend(corp_id):
    sql='SELECT a.id \
        ,a.sub_corp_name \
        ,avg(d.ph) as corp_ph \
        ,avg(d.conductivity) as corp_conductivity \
        ,avg(d.d_oxygen) as corp_DO \
        ,avg(d.rc) as corp_rc \
        ,avg(d.turbidity) as corp_turbidity \
        ,avg(d.temperature) as corp_temp \
        ,hour(d.send_time) as time \
        FROM device_watersubcorp a \
        LEFT JOIN device_watercorp b \
        ON a.corp_id = b.id \
        LEFT JOIN device_device c \
        ON a.id = c.sub_corp_id \
        LEFT JOIN hardsocket_water_param d \
        ON c.id = d.device_id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        LEFT JOIN device_area e \
        ON e.id = c.area_id \
        WHERE a.corp_id = %s \
        GROUP BY a.id,time \
        ORDER BY a.id'
    return __my_custome_sql(sql,corp_id)

def getSubCorpMonthTrend(corp_id):
    sql='SELECT a.id \
        ,a.sub_corp_name \
        ,avg(d.ph) as corp_ph \
        ,avg(d.conductivity) as corp_conductivity \
        ,avg(d.d_oxygen) as corp_DO \
        ,avg(d.rc) as corp_rc \
        ,avg(d.turbidity) as corp_turbidity \
        ,avg(d.temperature) as corp_temp \
        ,hour(d.send_time) as time \
        FROM device_watersubcorp a \
        LEFT JOIN device_watercorp b \
        ON a.corp_id = b.id \
        LEFT JOIN device_device c \
        ON a.id = c.sub_corp_id \
        LEFT JOIN hardsocket_water_param d \
        ON c.id = d.device_id \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        AND TO_DAYS(c.send_time) >= TO_DAYS(%s) \
        LEFT JOIN device_area e \
        ON e.id = c.area_id \
        WHERE a.corp_id = %s \
        GROUP BY a.id,time \
        ORDER BY a.id'
    return __my_custome_sql(sql,getFirstdayOfMonth(),getLastdayOfMonth(),corp_id)

#=============================================
def getOneSpotInfo(spot_id):
    sql = 'SELECT a.id as spot_id \
        ,c.corp_name as corp_name \
        ,d.area_name as area_name \
        ,b.device_info as spot_name \
        ,a.ph as spot_ph \
        ,a.conductivity as spot_conductivity \
        ,a.d_oxygen as spot_DO \
        ,a.rc as spot_rc \
        ,a.turbidity as spot_turbidity \
        ,a.temperature as spot_temp \
        ,a.send_time as last_time \
        FROM hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_watercorp c \
        ON b.corp_id = c.id \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        WHERE TO_DAYS(a.send_time) = TO_DAYS(NOW()) \
        AND a.device_id = %s \
        ORDER BY a.send_time DESC LIMIT 1'
    return __my_custome_sql(sql,spot_id)

#=============================================
def getSpotDetailInfo(spot_id):
    sql = 'SELECT a.id as spot_id \
        ,c.corp_name as corp_name \
        ,d.area_name as area_name \
        ,b.device_info as spot_name \
        ,a.ph as spot_ph \
        ,a.conductivity as spot_conductivity \
        ,a.d_oxygen as spot_DO \
        ,a.rc as spot_rc \
        ,a.turbidity as spot_turbidity \
        ,a.temperature as spot_temp \
        ,a.send_time as last_time \
        FROM hardsocket_water_param a \
        LEFT JOIN device_device b \
        ON a.device_id = b.id \
        LEFT JOIN device_watercorp c \
        ON b.corp_id = c.id \
        LEFT JOIN device_area d \
        ON b.area_id = d.id \
        WHERE TO_DAYS(a.send_time) = TO_DAYS(NOW()) \
        AND a.device_id = %s'
    return __my_custome_sql(sql,spot_id)

#=============================================


#=============================================



