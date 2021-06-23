# -*- coding: UTF-8 -*-
'''
@author: yhp
@date:20210621
@purpose:用户连接mysql数据库，返回cursor
'''
import pymysql
from datax

def conn_mysql():
    conn = pymysql.connect(host=cfgdb_m_host,
                           port=cfgdb_m_port,
                           user=cfgdb_m_dbuser,
                           passwd=cfgdb_m_password,
                           db=cfgdb_m_dbname,
                           charset=cfgdb_m_client_encoding)
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
