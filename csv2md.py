#!/usr/bin/env python
# -*-coding:utf8-*-
# author = felicitychou
# date = 2017/03/14
# support python 2

import sys
import csv

def main():

    with open(sys.argv[1], 'rb') as fr:
        reader = csv.reader(fr)
    
        first_row = True
        with open(sys.argv[2], 'wb') as fw:
            for row in reader:
                if first_row:
                    fw.write('|%s|\n' % ("|".join(row)))
                    fw.write('|%s\n' % ('---|'*len(row)))
                    first_row = False
                else:
                    fw.write('|%s|\n' % ("|".join(row)))

if __name__ == '__main__':
    main()

'''
usage: python csv2md.py *.csv *.md
'''