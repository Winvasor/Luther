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
system('clear')
def main():
   print NEGRI+A+'================================================'
   print '               CRIADO POR'+AZ+' WINVASOR'+A
   print '===================  2020  ====================='
   print '   ____            __  ___                   '
   print '  |    |    __ ___/  |_|  |__   ___________  ' 
   print '  |    |   |  |  \   __\  |  \_/ __ \_  __ \ '
   print '  |    |___|  |  /|  | |   Y  \  ___/|  | \/ '
   print '  |_______ \____/ |__| |___|  /\___ \|__|    '
   print '          \/                \/     \/     1.8'
   print AZ+'\a\tRun in Root User'+A
def indie():	
	print '[1] LUTHER-GMAIL'
	print '[2] LUTHER-PORTSCAN'
	print '[3] LUTTHER-FACE-BRUTE'
	print '[4] UPGRADE-LUTHER'
	print '[0] SAIR\n'
	
	OPCAO = raw_input('==>')

	if OPCAO == "1":
	   system('python2 libs/brute.py')

	elif OPCAO == "2":
		system('python libs/ps.py')
	elif OPCAO == "3":
		system('python libs/fb.py')


	elif OPCAO =="4":
		system('cd .. && rm -r Luther && git clone https://github.com/Winvasor/Luther.git && cd Luther && python2 lut.py')
	
	elif OPCAO == "0":
	   print AZ+'\nADEUS!!!\n\n'+NOR
	   sys.exit(1)
	else:
	   system('clear')
	   print AZ+'\n#404 NOT FOUND\n'+NOR
	   main()
	   indie()
main()
indie()
