#!/usr/bin/env python
# -*- coding:utf-8 -*-

''' 
install ssdeep

python 2
$ sudo apt-get install build-essential libffi-dev python python-dev python-pip libfuzzy-dev
Build and install Python module.

$ pip install ssdeep

python 3
$ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip libfuzzy-dev
Build and install Python module.

$ pip3 install ssdeep

https://python-ssdeep.readthedocs.io/en/latest/index.html
'''

import ssdeep

def ssdeep_file(file_path):
    return ssdeep.hash_from_file(file_path)

def ssdeep_big_file(file_path, max_size=1024):
    hash_handle = getattr(ssdeep,'Hash')()
    with open(file_path, 'rb') as file: 
            while True: 
                data = file.read(max_size) 
                if not data: 
                    break
                hash_handle.update(data)
    return h.digest()