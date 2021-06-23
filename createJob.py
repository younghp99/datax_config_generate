#-*- coding: UTF-8 -*-
'''
@author: yhp
'''
import json
from dataSource.textfile import writer,reader
from config.configModule import configModule
def create_job():
    job_reader_type='file'
    job_writer_type='file'
    job_settting_speed_channel=3
    file_name='/data/etl/etldata/filename.txt'
    fieldDelimiter=','
    column_list=''
    colunm_list=[]
    for i in range(0,3):
        colunm_list.append({"index":i,"type":"string"})
    configModule["job"]["setting"]["speed"]["channel"]=job_settting_speed_channel

    #file2file,构建输入输出源
    job_reader=reader('/data/etl/etldata/output/input.txt',colunm_list,',','true')
    job_writer=writer('/data/etl/etldata/output', 'output.txt', 'truncate', 'yyyy-MM-dd')
    configModule["job"]["content"]["reader"]=job_reader
    configModule["job"]["content"]["writer"]=job_writer
    #输出到文件
    with open("./resultJob/tableA2file.json", "w") as fp:
        fp.write(json.dumps(configModule,indent=4))

if __name__ == '__main__':
    create_job()