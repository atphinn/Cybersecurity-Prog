import os
import sqlite3
import optparse

# def printTables(iphoneDB):
#     try:
#         conn = sqlite3(iphoneDB)
#         c = conn.cursor()
#         c.execute('SELECT tbl_name FROM sqlite_master \
#         WHERE type==\"table\";')
#
#         print("\n[*] Database: " +iphoneDB)
#
#         for row in c:
#             print("[-] Table:" + str(row))
#
#     except:
#             pass
#     conn.close()
#
#     dirList = os.listdir(os.getcwd())
#     for fileName in dirList:
#         printTables(fileName)

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

def main():
    parser = optparse.OptionParser("usage%prog"+\
    "-p <iphone Backup Directory>")

    parser.add_option('-p', dest='pathName',\
    type='string',help='specify skype profile path')

    (options, args) = parser.parse_args()

    pathName = options.pathName
    if pathName == None:
        print(parser.usage)
        exit(0)
    else:
        dirList = os.listdir(pathName)
        for fileName in dirList:
            iphoneDB = os.path.join(pathName, fileName)

            if isMessageTable(iphoneDB):
                try:
                    print('\n[*] -- Found Messages --')
                    printMessage(iphoneDB)
                except:
                    pass

if __name__ == '__main__':
    main()
