#!/usr/bin/python2

'''CRIADO POR WINVASOR'''
 
import re
import sys,os
import random
import smtplib
from os import system

A = '\033[33m'
AZ = '\033[31m'
NEGRI = '\033[1m'
NOR = '\033[0;0m'
   
def main():
   
   system('clear')
   print NEGRI+A+'================================================'
   print '               CRIADO POR'+AZ+' WINVASOR'+A
   print '===================  2019  ====================='
   print '   ____            __  ___                   '
   print '  |    |    __ ___/  |_|  |__   ___________  ' 
   print '  |    |   |  |  \   __\  |  \_/ __ \_  __ \ '
   print '  |    |___|  |  /|  | |   Y  \  ___/|  | \/ '
   print '  |_______ \____/ |__| |___|  /\___ \|__|    '
   print '          \/                \/     \/     1.2'

main()
	
print '[1] LUTHER-GMAIL'
print '[2] LUTHER-FTP'
print '[0] SAIR\n'
OPCAO = input('==>')

if OPCAO == 1:
   system('python2 libs/brute.py')

elif OPCAO == 2:
	ip = raw_input('INSIRA O HOSTNAME/IP: ')
	user = raw_input('INSIRA O NOME DE USUARIO: ')
	PASS = raw_input('INSIRA A WORDLIST: ')
	system('python2 libs/ftp.py -t '+ip+' -u '+user+' -w '+PASS)
elif OPCAO == 0:
   print AZ+'\nADEUS!!!'+NOR
   exit()
else:
   print AZ+'\n#404 NOT FOUND'+NOR
