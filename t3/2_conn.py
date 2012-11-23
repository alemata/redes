#!/usr/bin/python

from scapy.all import *
import socket

def connectScann(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, port))
		print ("port " + str(port) + "\t  Open!")
	except socket.error, e:
		print ("port " + str(port) + "\t  Close")
	return
#socket.getservbyport(port)

splitted = sys.argv[2].split('-')
pFrom = int(splitted[0])
pTo = int(splitted[1])
for x in range(pFrom, pTo+1):
	connectScann(sys.argv[1], x)

