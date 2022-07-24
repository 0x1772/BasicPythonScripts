#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires sudo privledges"
	sys.exit()
def main():
	try:
		print ('''Welcome to BasicPythonScripts''')
		def inicio1():
			while True:
				print ('''
1) Download Scripts
2) Visit Github
3) Help
			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while option0 == "1":
					print ('''
