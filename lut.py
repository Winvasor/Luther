#!/usr/bin/python2

'''CRIADO POR WINVASOR'''
 
import re
import sys,os
import random
import requests
import smtplib
from os import system,getuid

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
def checkConnection(host='https://google.com'):  # Connection check
    system('clear')
    try:
        req = requests.get(host, timeout=10)
        if req.status_code == 200:
            return True
    except:
        return False


if checkConnection() == False:
    print(NEGRI+AZ+'\n\n\a Nenhuma Rede Detectada, conecte-se a internet!!!\n\n')
    exit()

if getuid() == 0:
	print('')
else:
    print (NEGRI)
    print(
    "{0}\aExecute o Luther-Framework no '{1}sudo{0}'".format(AZ, A))
    print ('\n\n')
    exit()





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
		system('cd .. && rm -r Luther && git clone https://github.com/Winvasor/Luther.git && cd Luther && python lut.py')
	elif OPCAO == "0":
	   print AZ+'\nADEUS!!!\n\n'+NOR
	   sys.exit(1)
	elif OPCAO == "":
		system('clear')
		main()
		print(AZ+'\n\nNenhuma alternativa selecionada!!!\n\n'+A)
		indie()
		
	else:
	   system('clear')
	   print AZ+'\n#404 NOT FOUND\n'+NOR
	   main()
	   indie()
main()
indie()
