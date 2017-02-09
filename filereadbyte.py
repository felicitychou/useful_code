#!/usr/bin/env Python
# -*- coding:utf-8 -*-

'''
按字节读取文件，输出十六进制/十进制文件数据。
'''

def  filereadbyte(filepath,offset,end=0,len=32,dec=True):
    f = open(filepath ,'rb')
    f.seek(offset,0)
    result = []
    i = 0
    while i < len:
        byte = f.read(1)
        if byte == '':
            break
        else:
            hexstr =  "%s" % byte.encode('hex')
            decnum = int(hexstr, 16)
            if decnum != end:
                if dec:
                    result.append(decnum)
                else:
                    result.append(hexstr)
                i = i+1
            else:
                break

    f.close()
    return result