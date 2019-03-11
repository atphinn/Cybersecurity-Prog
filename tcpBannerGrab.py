import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVuns(banner):
    if 'FreeFloat Ftp Server(Version 1.00)' in banner:
        print ('[+] FreeFlot FTP Server in vulnerable')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print ('[+] 3CDaemon FTP Server is vulnerable')
    elif 'Ability Server 2.34' in banner:
        print ('[+] Ability FTP Server is vulnerable')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable')
    else:
        print('[-]FTP Server is not vulnerable')
    return

def main():

    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip2 = '192.168.95.150'
    port = 21

    banner1 = retBanner(ip1,port)
    if banner1:
        print ('[+]' + ip1 + ':' + banner)
        checkVuns(banner1)

    banner2 = retBanner(ip2,port)
    if banner2:
        print ('[+]' + ip2 + ':x' + banner2)
        checkVuns(banner2)

    banner3 = retBanner(ip3,port)
    if banner3:
            print ('[+]' + ip3 + ':x' + banner3)
            checkVuns(banner3)

    if __name__ == '__main__':
        main()
