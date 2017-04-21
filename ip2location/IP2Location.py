#!/usr/bin/env python
# -*-coding:utf8-*-
# author = felicitychou
# date = 2017/4/14
# support python 2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class ipip(object):

    def __init__(self,dbpath):
        from ipip.ipip import IP
        self.IP = IP()
        self.IP.load(dbpath)

    def search(self,ip):
        return [item.encode('GBK') for item in self.IP.find(ip).split('\t')[:-1]]


class cz88(object):
    
    def __init__(self,dbpath):
        from cz88.qqwry import QQWry
        self.QQWry = QQWry(dbpath)

    def search(self,ip):
        # str
        return self.QQWry.query(ip)

class geoip(object):
    
    def __init__(self,dbpath):
        import maxminddb
        self.reader = maxminddb.open_database(dbpath)
        self.langs = ['zh-CN','en']

    def getcountry(self,ip):
        for lang in self.langs:
            country = self.reader.get(ip)['country']['names'].get(lang,None)
            if country:
                return country
        else:
            return ''

    def getsubdivisions(self,ip):
        if not self.reader.get(ip).get('subdivisions',None):
            return ''
        for lang in self.langs:
            subdivisions = self.reader.get(ip)['subdivisions'][0]['names'].get(lang,None)
            if subdivisions:
                return subdivisions
        else:
            return ''
    
    def getcity(self,ip):
        if not self.reader.get(ip).get('city',None):
                return ''
        for lang in self.langs:
            city = self.reader.get(ip)['city']['names'].get(lang,None)
            if city:
                return city
        else:
            return ''        
        
    def search(self,ip):
        country = self.getcountry(ip)
        subdivisions = self.getsubdivisions(ip)
        city = self.getcity(ip)
        return [country.encode('GBK'),subdivisions.encode('GBK'),city.encode('GBK')]
