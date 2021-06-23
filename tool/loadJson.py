#-*- coding: UTF-8 -*-
'''
purpose：暂时不用
@author: yhp
'''
import json
def loadJson(str):
    str=json.dumps(str)
    str_st=str[0:1]
    str_ed=str[-1:]
    print(str_st)
    print(str_ed)
    if str_st=='[':
        str=str[1:]
    if str_ed==']':
        str=str[:-1]
    print(len(str))
    return json.loads(str)


if __name__ == '__main__':
    print(111)