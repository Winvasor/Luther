#!/usr/bin/python

'''CRIADO POR WINVASOR'''

import socket
from os import system
print ("\n\n\a\tAVISO: O arquivo de log ficara na pasta libs\n\n")
site = raw_input("Insira o Server ==> ")
count = 1
print ('\n\a\t' + site + '\n\n\n')
while count <= 999999:
	client = socket.socket(socket.AF_INET, 	socket.SOCK_STREAM)
	client.settimeout(0.5)
	code = client.connect_ex((site, count))
	if code == 0:
		count2 = str(count)
		system('echo "' + count2 + ' OPEN" >> libs/log-port_scan.txt')
		print (count, "\a\tOPEN")
	else:
		print (count, "\a\tCLOSE")
	count = count + 1

