# -*- coding: UTF-8 -*-
'''
@author: yhp
@date:20210621
@purpose:用户连接mysql数据库，返回cursor
'''
import pymysql
from config.dbconfig import datax_db_m_host,datax_db_m_client_encoding,datax_db_m_dbname,datax_db_m_dbuser,datax_db_m_port,datax_db_m_password

def conn_mysql():
    conn = pymysql.connect(host=datax_db_m_host,
                           port=datax_db_m_port,
                           user=datax_db_m_dbuser,
                           passwd=datax_db_m_password,
                           db=datax_db_m_dbname,
                           charset=datax_db_m_client_encoding)
    return conn

def exe_sql(exesql):
    conn = conn_mysql()
    cursor = conn.cursor()
    cursor.execute(exesql)
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    print(exe_sql('select version();'))
