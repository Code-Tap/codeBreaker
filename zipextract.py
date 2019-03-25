#!/usr/bin/python

import zipfile, sys

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        print (f"[+] Found password = {password}")
        return True
    except:
        return False

def main():
    zname = r"test1.zip"
    zFile = zipfile.ZipFile(zname, 'r')

    for password in range(0,999):
        found = extractFile(zFile, str(password))
        if found == True:
                sys.exit()

    # If it makes it here password has not been found...
    print ('[-] Password not found')

if __name__ == "__main__":
    main()