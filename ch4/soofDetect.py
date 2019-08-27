from scapy.all import *
from IPy import IP as IPTEST
import time
import optparse

ttlValue = {}
THREASH = 5

def checkTTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype()=='PRIVATE':
        return

    if not ttlValues.has_key(ipsrc):
        pkt = sr1(IP(dest=ipsrc)/ICMP(),\
            retry=0,timeout=1,verbose=0)
        
        ttlValues[ipsrc] = pkt.ttl

    if abs(int(ttl)-int(ttlValues[ipsrc])) > THREASH:
        print('\n[!] Detected possible spoofed packet from:'\
            +ipsrc)

        print('[!]TTL:' + ttl+', Actual TTL:'\
            + str(ttlValue[ipsrc]))

def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            # print("[+]PKT recived from:" +ipsrc+"with TTL"\
            #     + ttl)
            checkTTL(ipsrc,ttl)
    except:
        pass


def main():

    parser = optparse.OptionParser("Usage%prog" +\
        "-i <interface> -t <thresh>")
    
    parser.add_option('-i', dest='iface', type='string',\
        help='specify network interface')
    parser.add_option('-t', dest='threash', type='string',\
        help='specify a threashold count')
    
    (options,args) = parser.parse_args()

    if options.iface == None:
        conf.iface ='eth0'
    else:
        conf.options.iface
    if options.threash != None:
        THREASH = options.threash
    else:
        THREASH = 5
        
    sniff(prn=testTTL, store=0)

if __name__ == '__main__':
    main()
