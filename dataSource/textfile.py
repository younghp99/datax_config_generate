#-*- coding: UTF-8 -*-
'''
purpose：文件类型数据源的读取和写入配置
@author: yhp
'''
def file_reader(path,column_list,fieldDelimiter,skipHeader='false'):
    #print("start create reader")
    name='txtfilereader'
    path=[path]
    encoding='UTF-8'
    column_list=column_list
    fieldDelimiter=fieldDelimiter
    reader={
        "name":name,
        "parameter": {
            "path": path,
            "encoding": encoding,
            "column": column_list,
            "fieldDelimiter": fieldDelimiter,
            "skipHeader":skipHeader
        }
    }
    #print(reader)
    return reader

def file_writer(path,filename,writeMode,format):
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
    print(file_reader('/aa/aa',[{"a":"a"},{"b":"b"}],','))
    print(file_reader('/aa/aa',[{"a":"a"},{"b":"b"}],',','true'))
    print(file_writer('/aa/aa','output.txt','truncate','yyyy-MM-dd'))