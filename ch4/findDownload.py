#http://sourceforge.net/projects/loic/

import dpkt
import socket

def findDwonload(pcap):
    for(ts, buf) in pcap:
        try:
            eth = dkpt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip, src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)

            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print('[!]' + src + 'Downloaded LOIC.')
        except:
            pass
    
        f = open()
        pcap = dpkt.pcap.Reader(f)
        findDwonload(pcap)