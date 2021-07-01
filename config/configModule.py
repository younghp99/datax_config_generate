#-*- coding: UTF-8 -*-
'''
purpose：
@author: yhp
'''
from dataSource.textfile import file_writer,file_reader
configModule={
    "job":{
        "setting":{
            "speed": {
            "channel": 2
            }
        },
        "content":[
            {}
        ]
    }
}
if __name__ == '__main__':
    print(configModule["job"]["content"])
    configModule["job"]["content"]["reader"]=file_reader('/aa/aa', [{"a": "a"}, {"b": "b"}], ',', 'true')
    configModule["job"]["content"]["writer"]=file_writer('/aa/aa', 'output.txt', 'truncate', 'yyyy-MM-dd')
    print(configModule["job"]["content"])
