#!/usr/bin/env python
#-*-coding:utf8-*-
# python 2/3

import hashlib
import os
import binascii

# hashlib ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
# base64
# binascii.crc32
# print '%x' % (binascii.crc32(data) & 0xffffffff)

def hash_big_file(file_path, hash_type, max_size=1024):

    if hasattr(hashlib,hash_type):
        
        hash_handle = getattr(hashlib,hash_type)()

        with open(file_path, 'rb') as file: 
            while True: 
                data = file.read(max_size) 
                if not data: 
                    break
                hash_handle.update(data)

        return hash_handle.hexdigest()

    if hash_type == 'crc32' and hasattr(binascii,hash_type):

        hash_handle = getattr(binascii,hash_type)()

        with open(file_path, 'rb') as file:
            crc32 = 0
            while True:
                data = file.read(max_size)
                if not data:
                    break
                crc32 = hash_handle(data,crc32)
        return '%x' % (crc32 & 0xffffffff)


def hash_file(file_path, hash_type):

    if hasattr(hashlib,hash_type):
        hash_handle = getattr(hashlib,hash_type)()

        with open(file_path, 'rb') as file: 
            hash_handle.update(file.read())

        return hash_handle.hexdigest()

    if hash_type == 'crc32' and hasattr(binascii,hash_type):
        hash_handle = getattr(binascii,hash_type)()
        
        with open(file_path, 'rb') as file:
            return '%x' % (hash_handle(file.read()) & 0xffffffff)


def hash_str(buffer, hash_type):
    if hasattr(hashlib,hash_type):
        hash_handle = getattr(hashlib,hash_type)()

        hash_handle.update(buffer)

        return hash_handle.hexdigest()

    if hash_type == 'crc32' and hasattr(binascii,hash_type):
        hash_handle = getattr(binascii,hash_type)()
        return '%x' % (hash_handle(buffer) & 0xffffffff)


def main(file_path, hash_type):

    if os.path.getsize(file_path) > 10*1024**2:
        print("%s Cal:%s\nSize:%d\n%s:%s" % (hash_type, file_path, os.path.getsize(file_path), hash_type, hash_big_file(file_path, hash_type)))
        #hash_big_file(file_path, hash_type)
    else:
        print("%s Cal:%s\nSize:%d\n%s:%s" % (hash_type, file_path, os.path.getsize(file_path), hash_type, hash_file(file_path, hash_type)))
        #hash_file(file_path, hash_type)



if __name__ == '__main__':

    small_file_path = ''
    big_file_path  = ''

    for hash_type in ['sha256','md5','crc32']:
        main(file_path=small_file_path, hash_type=hash_type)
        main(file_path=big_file_path, hash_type=hash_type)
    
    buffer = b'Hello World'

    for hash_type in ['sha256','md5','crc32']:
        print("%s Cal: %s\n%s:%s" % (hash_type, buffer, hash_type, hash_str(buffer=buffer,hash_type=hash_type)))


'''
rhash --crc32 --sha256 --md5 test
test  4a17b156  b10a8db164e0754105b7a99be72e3fe5  a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

rhash --crc32 --sha256 --md5 cranky_varahamihira.tar 
cranky_varahamihira.tar  7269a361  fdb719db73e6501829c578cb909a2708  b10e8b7da9747caf49bb92a8a12cb847ace1f0cd5fa85f874f84348d26c1e11c

python3 hash_cal.py 
sha256 Cal:test
Size:11
sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

sha256 Cal:cranky_varahamihira.tar
Size:116638720
sha256:b10e8b7da9747caf49bb92a8a12cb847ace1f0cd5fa85f874f84348d26c1e11c

md5 Cal:test
Size:11
md5:b10a8db164e0754105b7a99be72e3fe5
md5 Cal:cranky_varahamihira.tar
Size:116638720
md5:fdb719db73e6501829c578cb909a2708

crc32 Cal:test
Size:11
crc32:4a17b156

crc32 Cal:cranky_varahamihira.tar
Size:116638720
crc32:7269a361

sha256 Cal: b'Hello World'
sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

md5 Cal: b'Hello World'
md5:b10a8db164e0754105b7a99be72e3fe5

crc32 Cal: b'Hello World'
crc32:4a17b156


#python hash_cal.py 
sha256 Cal:test
Size:11
sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

sha256 Cal:cranky_varahamihira.tar
Size:116638720
sha256:b10e8b7da9747caf49bb92a8a12cb847ace1f0cd5fa85f874f84348d26c1e11c

md5 Cal:test
Size:11
md5:b10a8db164e0754105b7a99be72e3fe5

md5 Cal:cranky_varahamihira.tar
Size:116638720
md5:fdb719db73e6501829c578cb909a2708

crc32 Cal:test
Size:11
crc32:4a17b156

crc32 Cal:cranky_varahamihira.tar
Size:116638720
crc32:7269a361

sha256 Cal: Hello World
sha256:a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

md5 Cal: Hello World
md5:b10a8db164e0754105b7a99be72e3fe5
crc32 Cal: Hello World
crc32:4a17b156
'''