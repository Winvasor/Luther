#!/usr/bin/python

'''CRIADO POR WINVASOR'''

import socket
from os import system
A = '\033[33m'
AZ = '\033[31m'
def port_img():
	
	system('clear')

	print  '+=========================================+'
	print  '|..........' + AZ + '  Port -- Scanner  '+A+' ...........| '
	print  '+-----------------------------------------+'
system("clear")
port_img()
print ("\n\n\a\tAVISO: O arquivo de log ficara na pasta libs\n\n")
site = raw_input("Insira o Server ==> ")
time = input("Insira o TimeOut ==> ")
caminholog = ("libs/")
count = 1
print ('\n\a\t' + site + '\n\n\n')
try:
	while count <= 65535:
		client = socket.socket(socket.AF_INET, 	socket.SOCK_STREAM)
		client.settimeout(time)
		code = client.connect_ex((site, count))
		if code == 0:
			count2 = str(count)
			system('echo "' + count2 + ' OPEN" >> '+ caminholog + site +'-log-port.txt')
			print count, "\a\tOPEN"
		else:
				print count, "\a\tCLOSE"
		count = count + 1	
		
except KeyboardInterrupt as e:
	try:
		system("clear")
		port_img()
		system('cat '+ caminholog + site +'-log-port.txt')

	except cat as e:
		print("Nenhuma Port Aberta encontrada")
