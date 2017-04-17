#!/usr/bin/env python
# -*-coding:utf8-*-
# author = felicitychou
# date = 2017/4/14
# support python 2


import ConfigParser
import IP2Location


def loadconfig(confpath='conf'):
    confp = ConfigParser.ConfigParser()
    confp.read(confpath)
    #searchers = [getattr(IP2Location,sec)(dbpath=confp.get(sec,'dbpath')) for sec in confp.sections()]
    searchers = {}
    for sec in confp.sections():
        searchers[sec] = getattr(IP2Location,sec)(dbpath=confp.get(sec,'dbpath'))
    return searchers
    
            

def main(ips):
    
    searchers = loadconfig()
    for ip in ips:
        print r'%s'% (ip,)
        for name,searcher in searchers.iteritems():
            result =  searcher.search(ip)
            print r'%s:' % (name,),
            for item in result:
                print item,
            print ''
        

if __name__ == '__main__':
    #main()

    import argparse
    parser = argparse.ArgumentParser(prog='ip2location',description='IP address to location')
    parser.add_argument("-s",dest='ips',action='store',help='search ip to IP address.')
    args = parser.parse_args()
    if args.ips:
        main(args.ips)
    else:
        parser.print_help()
        sys.exit(0)