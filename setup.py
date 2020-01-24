#!/usr/bin/python

'''Setup for Luther-framework by winvasor'''

from os import system

try:
	system('cp libs/loots/lut /usr/bin/ && chmod +x /bin/lut')
	system('cp -r libs/loots/Luther-framework/ /opt/')
except:
    system('chmod +x setup.py')
    system('&& python setup.py')


