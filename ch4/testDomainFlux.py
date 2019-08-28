#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from scapy.all import *

def dnsQRTTest(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode

        qname = pkt.getlayer(DNSQR).qname

        if rcode == 3:
            print('[!] Name request lookup failed:' + qname)
            return True
        
        else: 
            return False


def main():
    unAnsReqs = 0
    pkts = rdpcap('domainFlux.pcap')
    for pkt in pkts:
        if dnsQRTTest(pkt):
            unAnsReqs = unAnsReqs + 1
    
    print('[!]' + str(unAnsReqs)+ 'Total Unanswered Name Request')

if __name__ == '__main__':
    main()



