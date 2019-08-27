form scapy.all import *

def testTTL(pkt):
    try:
        if pkt.haslayer(ip):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            print("[+]PKT recived from:" +ipsrc+"with TTL"\
                + ttl)
    
    except:
        pass


def main():
    sniff(prn=testTTL, store =0)

if __name__ == '__main__':
    main()
