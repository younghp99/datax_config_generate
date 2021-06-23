# -*- coding: UTF-8 -*-
'''
@author: yhp
@date:20210618
@purpose:用户连接pg数据库，返回cursor
'''
import psycopg2
from config.dbconfig import cfgdb_dbname, cfgdb_dbuser, cfgdb_password, cfgdb_host, cfgdb_port, cfgdb_client_encoding


def conn_pg():
    ## 连接到一个给定的数据库
    # conn = psycopg2.connect(dbname="zbedw", user="postgres", password="postgres",
    #                        port="5432", host="localhost", client_encoding="UTF-8")
    conn = psycopg2.connect(dbname=cfgdb_dbname, user=cfgdb_dbuser, password=cfgdb_password,
                            port=cfgdb_port, host=cfgdb_host, client_encoding=cfgdb_client_encoding)
    return conn


def exe_sql(exesql):
    try:
        # 连接到一个给定的数据库
        conn = conn_pg()
        cursor = conn.cursor()
        ## 执行SQL SELECT命令

        cursor.execute(exesql)
        ## 获取SELECT返回的元组
        rows = cursor.fetchall()
        cursor.close()
    except Exception:  # 方法一：捕获所有异常
        # 如果发生异常，则回滚
        print("发生异常", Exception)
        conn.rollback()
    finally:
        # 最终关闭数据库连接
        conn.close()
    return rows


if __name__ == '__main__':
    conn_pg()
    print(exe_sql('select count(1) from dsa.fld_load_cfg'))
