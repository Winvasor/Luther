#!/usr/bin/python

'''CRIADO POR WINVASOR'''

import socket
from os import system
def port_img():
	print ('''
	_________________ ____________________/\     
	\______   \   _  \\______   \__    ___)/_____
	 |     ___/  /_\  \|       _/ |    |  /  ___/
	 |    |   \  \_/   \    |   \ |    |  \___ \ 
	 |____|    \_____  /____|_  / |____| /____  >
	                 \/       \/              \/ ''')
system("clear")
port_img()
print ("\n\n\a\tAVISO: O arquivo de log ficara na pasta libs\n\n")
site = raw_input("Insira o Server ==> ")
time = input("Insira o TimeOut ==> ")
resp = raw_input("Deseja salvar um arquivo de log com as porta? [S-N] ==> ")
if resp == "S" or resp == "s":
			caminholog = raw_input("Insira caminho para salvar o LOG ==> ")
count = 1
print ('\n\a\t' + site + '\n\n\n')
try:
	while count <= 65535:
		client = socket.socket(socket.AF_INET, 	socket.SOCK_STREAM)
		client.settimeout(time)
		code = client.connect_ex((site, count))
		if resp == "N" or resp == "n":
			if code == 0:
				count2 = str(count)
				print count, "\a\tOPEN"
			else:
				print count, "\a\tCLOSE"
		else:
			if code == 0:
				count2 = str(count)
				system('echo "' + count2 + ' OPEN" >> '+ caminholog + site +'/log-port_scan.txt')
				print count, "\a\tOPEN"
			else:
				print count, "\a\tCLOSE"
		count = count + 1	
		
except KeyboardInterrupt as e:
	try:
		system("clear")
		port_img()
		system('cat '+ caminholog + site +'/log-port_scan.txt')

	except bash as e:
		print("Nenhuma Port Aberta encontrada")
