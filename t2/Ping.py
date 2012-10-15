#!/usr/bin/python

from scapy.all import *


def ping(host):
	packet = IP(dst=host)/ ICMP() / "Soy ale, hice un ping"
	start = time.time()
	ans = sr1(packet, timeout=60, verbose=0)
	if not (ans is None):
		#ans.show2()
		elapsed = (time.time() - start)
		#print "Time = %s" % elapsed	
		return elapsed;
	else:
		#print "Timeout waiting for %s" % packet[IP].src
		return -1 # si fallo mando -1 para saber que es un tiempo invalido

