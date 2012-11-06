#!/usr/bin/python

from scapy.all import *
import socket

def synScann(host, port):
	ans = sr1(IP(dst=host)/TCP(dport=(port),flags="S"), timeout=3 , verbose=0)
	if not (ans is None):
		#Si hay respuesta TCP, me fijo los flags y categorizo
		if ans.haslayer(TCP) :
			if ans[TCP].flags == 20:
				print ("port " + str(ans[TCP].sport) + "\t  Close")
			if  ans[TCP].flags == 18:
				print ("port " + str(ans[TCP].sport) + "\t  Open!")
		if ans is ICMP and ans.payload.type == 3:
			print ("port " + str(ans[TCP].sport) + "\t  Filtered(ICMP)")	
	else:
		print ("port " + str(ans[TCP].sport) + "\t  Filtered")
	return
#socket.getservbyport(port)
#ans.sprintf("%TCP.sport% \t %TCP.flags%")

def synScann2(host, port):
	ans, unans = sr(IP(dst=host)/TCP(dport=(port),flags="S"),timeout=3, verbose=0)
	ans.summary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA",prn=lambda(s,r):r.sprintf("port " + str(port) + "\t Open!"))
	ans.summary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "RA",prn=lambda(s,r):r.sprintf("port " + str(port) + "\t Close"))
	ans.summary(lfilter = lambda (s,r): r.sprintf("%ICMP.type%") == "3",prn=lambda(s,r):r.sprintf("port " + str(port) + "\t Filtered(ICMP)"))
	unans.summary(prn=lambda(s):s.sprintf("port " + str(port) + "(%TCP.sport%) \t is Filtered"))

splitted = sys.argv[2].split('-')
pFrom = int(splitted[0])
pTo = int(splitted[1])
for x in range(pFrom, pTo):
	synScann2(sys.argv[1], x)

