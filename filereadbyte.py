#!/usr/bin/env Python
# -*- coding:utf-8 -*-

import binascii
'''
按字节读取文件，输出十六进制/十进制文件数据。
'''
'''
def  filereadbyte(filepath,offset,end=0,len=32,dec=True):
    f = open(filepath ,'rb')
    f.seek(offset,0)
    result = []
    i = 0
    while i < len:
        byte = f.read(1)
        # read no data
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
'''

# 读取文件，输出文件内容的十六进制字符串。offset/指定文件偏移 end/指定结束标志 len/指定读取内容长度
# end与len，优先生效end。 end指定为某个十六进制值/或某个字符，比如 end='\x00'，end='a'

def filereadhex(filepath,offset=0,end='',length=0):
    with open(filepath,'rb') as file:
        file.seek(offset,0)

        if end:
            data = file.read()
            return binascii.hexlify(data[:data.find(end)])

        if length:
            return binascii.hexlify(f.read(length))

        return binascii.hexlify(f.read())





# 按长度切割字符串

def strcut(string,width):
    return [string[x:x+width] for x in range(0,len(string),width)]


# 生成固定长度随机字符串
'''
https://www.oschina.net/code/snippet_153443_4752
''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16)))

>>> data = os.urandom(16)
>>> ''.join(map(lambda x:(hex(ord(x))[2:]),data))
'5ef4814896ae898c2a8933b1481a9216'
>>> import binascii
>>> print binascii.hexlify(data)
5ef4814896ae898c2a8933b1481a9216
'''

def randomstr1(length):
    import os
    return ''.join(map(lambda x:(hex(ord(x))[2:]),os.urandom((length+1)/2)))[:length]

def randomstr2(length):
    import os,binascii
    return binascii.hexlify(os.urandom((length+1)/2))[:length]
