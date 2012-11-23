#!/usr/bin/python

from scapy.all import *
import socket

def synScann(host, port):
	ans = sr1(IP(dst=host)/TCP(dport=(port),flags="S"), timeout=3 , verbose=0)
	if not (ans is None):
		if ans.sprintf("%TCP.flags%") == "SA":
			print ("port " + str(ans[TCP].sport) + "\t  Open!")
		elif ans.sprintf("%TCP.flags%") == "RA":	
			print ("port " + str(ans[TCP].sport) + "\t  Close")
		elif ans is ICMP and ans.payload.type == 3:
			print ("port " + str(ans[TCP].sport) + "\t  Filtered(ICMP)")	
	else:
		print ("port " + str(port) + "\t  Filtered")
	return
#socket.getservbyport(port)

splitted = sys.argv[2].split('-')
pFrom = int(splitted[0])
pTo = int(splitted[1])
for x in range(pFrom, pTo+1):
	synScann(sys.argv[1], x)

