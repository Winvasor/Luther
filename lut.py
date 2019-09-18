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
   print '          \/                \/     \/     1.1'

main()

print '[1] LUTHER-GMAIL'
print '[0] SAIR\n'
OPCAO = input('==>')

if OPCAO == 1:
   system('python2 libs/brute.py')

elif OPCAO == 0:
   print AZ+'\nADEUS!!!'+NOR
   exit()
else:
   print AZ+'\n#404 NOT FOUND'+NOR
