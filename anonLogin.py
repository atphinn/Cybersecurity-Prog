import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print('\n[*]' + str(hostname) + \
            'FTP Anonymous login succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-]' + str(hostname) +\
            'FTP Anonymous login failed')
        return False

host = '192.168.95.179'
anonLogin(host)    
