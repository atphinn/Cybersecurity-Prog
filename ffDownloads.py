import sqlite3

def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT name, source, datetime(endTime/1000000,\
    \'unixepoch\') FROM moz_downloads;'
    )

    print('\n[*] ---Files Downloaded---')

    for row in c:
        print('[+]File:' +str(row[0])+ 'from source:'\
        + str(row[1])+ 'at: '+ str(row[2]))

def main():
        print('[+] Starting.....')


if __name__ == "__main__":
    main ()