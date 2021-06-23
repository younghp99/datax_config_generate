#-*- coding: UTF-8 -*-
'''
@author: yhp
'''
import json
from datax.tool import loadJson


def TxtFile(filename):
    filename=filename
    str='''{
    "setting": {},
    "job": {
        "setting": {
            "speed": {
                "channel": 2
            }
        },
        "content": [
            {
                "reader": {
                    "name": "txtfilereader",
                    "parameter": {
                        "path": ["/home/haiwei.luo/case00/data"],
                        "encoding": "UTF-8",
                        "column": [
                            {
                                "index": 0,
                                "type": "long"
                            },
                            {
                                "index": 1,
                                "type": "boolean"
                            },
                            {
                                "index": 2,
                                "type": "double"
                            },
                            {
                                "index": 3,
                                "type": "string"
                            },
                            {
                                "index": 4,
                                "type": "date",
                                "format": "yyyy.MM.dd"
                            }
                        ],
                        "fieldDelimiter": ","
                    }
                },
                "writer": {
                    "name": "txtfilewriter",
                    "parameter": {
                        "path": "/home/haiwei.luo/case00/result",
                        "fileName": "luohw",
                        "writeMode": "truncate",
                        "format": "yyyy-MM-dd"
                    }
                }
            }
        ]
    }
}'''

    str_json=json.loads(str)
    #print(json.dumps(str_json["job"]["content"])[1:-1])
    content_str=json.loads(json.dumps(str_json["job"]["content"])[1:-1])
    print(content_str)
    #print(content_str["reader"]["parameter"]["column"])

    con= loadJson.loadJson(str_json["job"]["content"])
    print(loadJson.loadJson(con["reader"]["parameter"]["column"]))

TxtFile('name')
