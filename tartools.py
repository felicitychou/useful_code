#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tarfile



# 打包
# packpath是一个文件，则打包后的文件名为 文件名.tar
# packpath是一个文件夹, 则打包后的文件名为 文件夹.tar，保持原文件夹的组织关系
# tarpath可以指定文件打包后的文件夹
def pack(packpath,tarpath=''):

    packpath = os.path.abspath(packpath)

    if not os.path.exists(packpath):
        return

    if os.path.isdir(packpath):
        dirname = packpath.split(os.path.sep)[-1]
        tarpath = tarpath if tarpath else "%s.tar" % dirname
        with tarfile.open(tarpath,'w') as tar:
            for root,dir,files in os.walk(packpath):  
                for file in files:  
                    fullpath=os.path.join(root,file)
                    arcname = os.path.join(dirname,os.path.relpath(fullpath,packpath))
                    tar.add(fullpath,arcname=arcname)
        return

    if os.path.isfile(packpath):
        filename = os.path.basename(packpath)
        tarpath = tarpath if tarpath else "%s.tar" % filename
        with tarfile.open(tarpath,'w') as tar:
            tar.add(os.path.abspath(packpath),arcname=filename)
        return


# 解包
# tarpath 解包的文件路径 unpackpath 解包后的文件存放路径 delete_o 删除原文件
# 如果unpackpath 指定的文件夹不存在，则创建文件夹。如果unpackpath没有值，或者是一个文件，则解包到当前目录
def unpack(tarpath,unpackpath='',delete_o = False):
    tarpath = os.path.abspath(tarpath)

    if not os.path.exists(tarpath):
        print "%s not exists." % tarpath
        return

    if unpackpath and not os.path.exists(unpackpath):
        os.mkdir(unpackpath)

    unpackpath = unpackpath if unpackpath and os.path.isdir(unpackpath) else os.getcwd()    

    with tarfile.open(name=tarpath, mode='r') as tar:
        tar.extractall(path=unpackpath)
    
    if delete_o:
        os.remove(tarpath)
