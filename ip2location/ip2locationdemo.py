#!/usr/bin/env python
# -*-coding:utf8-*-
# author = felicitychou
# date = 2017/4/14
# support python 2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import ConfigParser
import argparse
import sys

import IP2Location


def loadconfig(confpath='conf'):
    confp = ConfigParser.ConfigParser()
    confp.read(confpath)
    searchers = {}
    for sec in confp.sections():
        searchers[sec] = getattr(IP2Location,sec)(dbpath=confp.get(sec,'dbpath'))
    return searchers
    
def show(results):
    for ip,result in results.iteritems():
        print '%s\t' % (ip),
        for name,location in result.iteritems():
            print "%s(%s)\t" % (",".join([item for item in location if item]),name),
        print ''

def output(results,out):
    with open(out,'w') as fw:
        first = True
        
        for ip,result in results.iteritems():
            if first:
                fw.write("%s,%s\n" % ("IP",",".join(results[ip].keys())))
                first = False
            fw.write('%s,' % (ip))
            for name,location in result.iteritems():
                fw.write("%s," % ("".join([item for item in location if item]),))
            fw.write('\n')


def main(ips,out=None):
    
    searchers = loadconfig()
    results = {}

    for ip in ips:
        ip = ip.strip()
        result = {}
        for name,searcher in searchers.iteritems(): 
            result[name] =  searcher.search(ip)
        results[ip] = result

    show(results)
    if out:
        output(results,out)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ip2locationdemo',description='IP address to location')
    parser.add_argument("-s",dest='ip',action='store',help='search ip to location.')
    parser.add_argument("-i",dest='ips',action='store',help='search ip to location from file.')
    parser.add_argument("-o",dest='out',action='store',help='search ip to location from file and store result to file.')
    args = parser.parse_args()
    if args.ip:
        main([args.ip],args.out)
    elif args.ips:
        with open(args.ips,'r') as fr:
            main(fr.readlines(),args.out)
    else:
        parser.print_help()
        sys.exit(0)