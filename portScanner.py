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
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable: "+banner.strip('\n'))

def main():
    portList = [21,22,25,80,110,443]
    ip1 = '192.168.1.3' + str(x)

    for port in portList:
     banne1 = retBanner(ip1,port)

     if banner1:
         print('[+]' + ip1 + ':' + banner)

    if __name__ == '__main__':
        main()
