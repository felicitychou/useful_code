# !/usr/bin/env python
# -*- coding: utf8 -*-
# not good

import time

from scapy.all import *

tcp_pkts = PacketList()
udp_pkts = PacketList()
other_pkts = PacketList()

pkts_list = {'tcp':tcp_pkts,'udp':udp_pkts,'other':other_pkts}

def savepkt(pkt,pkttype,pkts_list):
    pkts_list[pkttype].append(pkt)
    if len(pkts_list[pkttype]) == 500:
        wrpcap("%s_netdata_%s.pcap" % (pkttype,time.time()), pkts_list[pkttype])
        pkts_list[pkttype] = PacketList()
    else:
        pass

# 从数据包中筛选出tcp、udp包，并分开保存
def handler(pkt):
    global pkts_list
    if pkt.haslayer(TCP):
        savepkt(pkt,'tcp',pkts_list=pkts_list)
    elif pkt.haslayer(UDP):
        savepkt(pkt,'udp',pkts_list=pkts_list)
    else:
        savepkt(pkt,'other',pkts_list=pkts_list)


#sniff(iface='eth0',prn=handler)
sniff(offline="test.pcap", prn=handler, count=1500)


for pkttype in pkts_list:
    if pkts_list[pkttype]:
        wrpcap("%s_netdata_%s.pcap" % (pkttype,time.time()), pkts_list[pkttype])
    else:
        pass