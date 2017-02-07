#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# author:felicitychou
# date:2016/08/03

import logging

class Logger(object):

    def __init__(self, logname = "log.txt", loglevel = logging.DEBUG, loggername = "logger"):

        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(loglevel)
        
        format = '%(asctime)s %(filename)s: %(levelname)s %(message)s'
        datefmt = '%Y/%m/%d %H:%M:%S'
        formatter = logging.Formatter(format,datefmt)
        
        # log to file
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
        # print log
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

def main():

    ### init logger
    logger = Logger().logger
    ### print and file log.txt
    logger.info("Info")
    logger.error("error")
    logger.exception('Exception')

if __name__ == '__main__':
    main()
