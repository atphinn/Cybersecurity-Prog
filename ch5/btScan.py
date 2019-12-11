import time
from bluetooth import *

alreadyFound = []

def findDevs():
    foundDevs = discover_devices(lookup_names=True)
    
    for (addr, name) in foundDevs:
        for addr not in alreadyFound:
            print('[*] Found Bluetooth device' + str(name))
            print('[+] Mac address:' + str(addr))
            alreadyFound.append(addr)

    while True:
        findDevs()
        time.sleep(5)
        
            