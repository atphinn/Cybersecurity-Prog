import os
import sqlite3
import optparse

def printTables(iphoneDB):
    try:
        conn = sqlite3(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master \
        WHERE type==\"table\";')

        print("\n[*] Database: " +iphoneDB)

        for row in c:
            print("[-] Table:" + str(row))

    except:
            pass
    conn.close()

    dirList = os.listdir(os.getcwd())
    for fileName in dirList:
        printTables(fileName)

def isMessageTable(iphoneDB):
    try:
        conn = sqlite3(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master\
        WHERE type==\"table";')

        for row in c:
            if 'message' in str(row):
                return True
    except:
        return False

def printMessage(msgDB):
    try:
        conn = sqlite3(msgDB)
        c = conn.cursor()
        c.execute('SELECT datetime(date, \'unixepoch\'),\
        address, text FROM message WHERE address>0;')

        for row in c:
            date = str(row[0])
            addr = str(row[1])
            text = row[2]

            print('\n[+] Date: '+date+',Addr:'+addr \
            + 'Message:' + text)
    except:
        pass
