import dpkt
import socket
import optparse

THRESH = 10000

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

def findHivemind(pcap):
    for(ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport

            if dport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDos Hivemind issued by:' + src)
                    print('[+] Target CMD:' + tcp.data)
            
            if sport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDos Hivemind issued to:' + src)
                    print('[+] Target CMD:' + tcp.data)
        except:
            pass

def findAttack(pcap):
    pktCount= {}

    for(ts, buf) in pcap:
        try:
            eth = dkpt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.data

            if dport == 80:
                stream = src + ':' + dst

                if pktCount.has_key(stream):
                    pktCount[stream] = pktCount[stream] + 1
                
                else:
                    pktCount[stream] = 1
        except:
            pass

    for stream in pktCount:
        pktsSent = pktCount[stream]

        if pktsSent > THRESH:
            src = stream.split(':')[0]
            dst = stream.split(':')[1]
            print('[+]' + src + 'attacked'+dst+'with'\
                + str(pktsSent) + 'pkts')


def main():
    parser = optparse.OptionParser("Usage%prog" +\
        '-p <pcap file> -t <threshold>'
        )

    parser.add_option('-p', dest='pcapFile', type='string',\
        help='Specify the pcap filename')
    parser.add_option('-t', dest='thresh', type='string',\
        help='Specify threashold count')
    
    (options, args) = parser.parse_args()

    if options.pcapFile == None:
        print(parser.usage)

        exit(0)
    
    if options.thresh != None:
        THRESH = options.thresh
    
    pcapFile = options.pcapFile

    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f, encoding="ISO-8859-1")
    
    findDwonload(pcap)
    findHivemind(pcap)
    findAttack(pcap)

if __name__ == "__main__":
    main()