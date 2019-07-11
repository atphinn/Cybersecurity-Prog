# brutrLogin

import ftplib

def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split('.')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
    print('[+] Trying:' + userName +"/" + passWord)


    
    
