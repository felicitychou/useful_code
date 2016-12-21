#!/usr/bin/env python
#-*-coding:utf8-*-
# 

import hashlib
import os

# hashlib ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
# base64
# crc

def hash_big_file(file_path, hash_type, max_size=1024):

    hash_handle = getattr(hashlib,hash_type)()

    with open(file_path, 'rb') as file: 
        while True: 
            data = file.read(max_size) 
            if not data: 
                break
            hash_handle.update(data)

    return hash_handle.hexdigest()


def hash_file(file_path, hash_type):

    hash_handle = getattr(hashlib,hash_type)()

    with open(file_path, 'rb') as file: 
        hash_handle.update(file.read())

    return hash_handle.hexdigest()

def hash_str(buffer, hash_type):
    hash_handle = getattr(hashlib,hash_type)()

    hash_handle.update(buffer)

    return hash_handle.hexdigest()

def main(file_path, hash_type):

    if os.path.getsize(file_path) > 10*1024**2:
        print("%s Cal:%s\nSize:%d\n%s:%s" % (hash_type, file_path, os.path.getsize(file_path), hash_type, hash_big_file(file_path, hash_type)))
        #hash_big_file(file_path, hash_type)
    else:
        print("%s Cal:%s\nSize:%d\n%s:%s" % (hash_type, file_path, os.path.getsize(file_path), hash_type, hash_file(file_path, hash_type)))
        #hash_file(file_path, hash_type)

if __name__ == '__main__':

    #main(file_path='wget', hash_type='sha256')

    print(hash_str(buffer=b"lalalalla",hash_type='sha256'))