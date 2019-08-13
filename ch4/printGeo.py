import pygeoip

gi = pygeoip.GeoIP('/Users/alexanderphinn/Documents/Programming/Cybersecurity-Prog/ch4/GeoLite2-City_20190806/GeoLite2-City.mmdb')

def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region_name']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']

    print('[*]Target: '+tgt+'Geo-located.')
    print('[+]' +str(city)+','+str(region)+','+str(country))
    print('[+] Latitude: ' +str(lat)+',Longitude' + str(long))

    tgt = '192.168.169.3'
    printRecord(tgt)
