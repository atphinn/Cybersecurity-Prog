import parser
#import dpkt
import pylint.test.regrtest_data.package
import socket
import pygeoip
import optparse

def retKML(ip):
    rec = gi.record_by_name(ip)
    try:
        longitutde = rec['longitutde']
        latitude = rec['latitude']

        kml=(
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<coordinates>%6f%6f</coordinates>/n'
            '<Point>/n'
        )%(ip,longitutde,latitude)
    
        return kml
    
    except Exception as e:
        return '' 

def plotIPs(pcap):
    kmlPts = ''

    for (ts,buf) in pcap:
        try:
            eth = dkpt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            srcKML = retKML(src)
            dst = socket.inet_ntoa(ip.dst)
            dstKML = retKML(dst)
        
        except:
            pass
        
        return kmlPts

def main():
    parser = optparse.OptionParser('usage%prog -p <pcap file>')
    paser.add_option('-p', dest='pcapFile', typer='string',\
        help='specify pcap filename')
    
    (options, args) = parser.parse_args()

    if options.pcapFile == None:
        print (parser.usage)
        exit(0)
    f = open('geptest.pcap')
    pcap = dpkt.pcap.Reader(f)

    kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\
        \n <kml  xmlns="http://www.openis.net/kml/2.2">\n'

    kmlfooter = '</Document>\n </kml>\n'
    kmldoc = kmlheader + plotIPs(pcap)+kmlfooter
    print(kmldoc)

if __name__ == '__main__':
    main()
    