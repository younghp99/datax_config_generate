#-*- coding: UTF-8 -*-
'''
purpose：mysql数据源的读取和写入配置
@author: yhp
'''
import pymysql
from conn.conn_mysql import conn_mysql,exe_sql
def mysql_reader(dbname,column_list,tablename):
    #print("start create reader")
    name='mysqlreader'
    result=exe_sql("select * from dbconfig where sysname='"+dbname+"';")
    print(result)
    dbname=result[0][2]
    dbhost=result[0][3]
    dbport=result[0][4]
    username=result[0][5]
    passwd=result[0][6]
    jdbc_url="jdbc:mysql://"+dbhost+":"+dbport+"/"+dbname
    query_sql='select * from '+dbname+'.'+tablename+";"
    column_list=column_list
    reader={
        "name":name,
        "parameter": {
            "username": username,
            "password": passwd,
            "connection": [
                {
                    "querySql": [
                        query_sql
                    ],
                    "jdbcUrl": [
                        jdbc_url
                    ]
                }
            ]
        }
    }
    #print(reader)
    return reader

def mysql_writer(path,filename,writeMode,format):
    #print("start create writer")
    path=path
    filename=filename
    #truncate，写入前清理目录下一fileName前缀的所有文件。
    #append，写入前不做任何处理，DataX TxtFileWriter直接使用filename写入，并保证文件名不冲突。
    #nonConflict，如果目录下有fileName前缀的文件，直接报错。
    writeMode=writeMode
    format=format
    writer={
            "name": "txtfilewriter",
            "parameter": {
                "path": path,
                "fileName": filename,
                "writeMode": writeMode,
                "format": format
            }
    }
    #print(writer)
    return writer
if __name__ == '__main__':
    print(mysql_reader('DWMETA','','tab_load_cfg'))