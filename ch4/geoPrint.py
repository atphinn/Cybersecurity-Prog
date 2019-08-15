import pylint.test.regrtest_data.package
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP("/opt/GeoIP/Geo.dat")

def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']

        if city !='':
            geoLoc = city + ',' + country
        
        else:
            geoLoc = country
        
        return geoLoc
    except Exception as e:
            return 'Unregistered'

def printPcap(pcap):
    for(ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip,src)
            dst = socket.inet_ntoa(ip.dst)

            print('[+] Src:' + src + '--> Dst:' + dst)
            print('[+] Src:' + retGeoStr(src) + '--> Dst:' + retGeoStr(dst))

        except:
            pass

def main():

    parser = optparse.OptionParser('usage%prog -p <pcap file>')
    paser.add_option('-p', dest='pcapFile', typer='string',\
        help='specify pcap filename')
    
    (options, args) = parser.parse_args()

    if options.pcapFile == None:
        print parser.usage
        exit(0)
    f = open('geptest.pcap')
    pcap = dpkt.pcap.Reader(f)

    printPcap(pcap)

    
if __name__ == '__main__':
    main()
