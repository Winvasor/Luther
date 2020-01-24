#!/usr/bin/python

'''Setup for Luther-framework by winvasor'''

from os import system

#system('pip install -r requiriments.txt')
try:
	system('cp libs/loots/lut /usr/bin/ && chmod +x /bin/lut')
	system('cp -r libs/loots/Luther-framework/ /opt/')
except:
	try:
		system('chmod +x setup.py')
		system('^Z && python setup.py')
	except:
		print('run in root')

