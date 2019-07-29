from _winreg import *

def val2addr(val):
    addr = ""

    for ch in val:
        addr += ("%02x"% ord(ch))
    addr = addr.strip(" ").replace("", ":")[0:17]
    return addr

def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion"+\
        "\NETWORKList\Signatures\Unmanaged"
    
    key = OpenKey(HKEY_LOCAL_MACHINE, net)

    print("\n[*] Networks You have Joined")
    
    for i in range(100):
        try:
            guid = EnumKey(key,i)
            netKey = OpenKey(key,str(guid))
            (n, addr)
