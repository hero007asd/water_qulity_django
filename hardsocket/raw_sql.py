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



#=============================================



#=============================================
