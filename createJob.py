#-*- coding: UTF-8 -*-
'''
@author: yhp
'''
import json
from dataSource.textfile import file_reader,file_writer
from config.configModule import configModule
from conn.conn_mysql import conn_mysql,exe_sql
def get_job_parameter(job_nm):
    sql='select src_db_type,src_db_name,src_tab_name,src_etl_type,tgt_db_type,tgt_db_name,tgt_tab_name,tgt_load_type from job_cfg t where t.job_nm=\''+job_nm+'\';'
    result=exe_sql(sql)
    print(result[0])
    job={
        'src_db_type' :result[0][0],
        'src_db_name':result[0][1],
        'src_tab_name':result[0][2],
        'src_etl_type':result[0][3],
        'tgt_db_type':result[0][4],
        'tgt_db_name':result[0][5],
        'tgt_tab_name':result[0][6],
        'tgt_load_type':result[0][7]
    }
    print(job)
    return job

def create_job(job_nm):
    job_par=get_job_parameter(job_nm)
    reader_type=job_par['src_db_type']
    reader_name=job_par['src_db_name']
    reader_table_name=job_par['src_tab_name']
    reader_etl_type=job_par['src_etl_type']
    writer_type=job_par['tgt_db_type']
    writer_name=job_par['tgt_db_name']
    writer_table_name=job_par['tgt_tab_name']
    writer_load_type=job_par['tgt_load_type']
    job_settting_speed_channel=3
    fieldDelimiter=','
    column_list=[]
        #模拟构建列信息
    for i in range(0,3):
        column_list.append({"index":i,"type":"string"})
    #reader的逻辑处理
    if reader_name[:-1]!='/':
        reader_name+='/'
    # reader为file,还需要处理列信息
    if reader_type=='file':
        reader_name=reader_name+reader_table_name
        job_reader=file_reader(reader_name,column_list,fieldDelimiter,'true')

    #writer的处理逻辑
    # writer为file
    if writer_type=='file':
        job_writer=file_writer(writer_name, writer_table_name, writer_load_type, 'yyyy-MM-dd')

    #构建job配置内容
    configModule["job"]["content"]["reader"]=job_reader
    configModule["job"]["content"]["writer"]=job_writer
    configModule["job"]["setting"]["speed"]["channel"]=job_settting_speed_channel
    #将job配置内容输出到文件
    with open("./resultJob/"+job_nm+".json", "w") as fp:
        fp.write(json.dumps(configModule,indent=4))

if __name__ == '__main__':
    get_job_parameter('file2file')
    create_job('file2file')