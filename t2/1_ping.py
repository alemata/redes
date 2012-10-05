#!/usr/bin/python

from scapy.all import *


def ping(host, count=1):
  packet = IP(dst=host)/ ICMP() / "Soy ale, hice un ping"
  for x in range(count):
     start = time.time()
     ans = sr1(packet, timeout=60)
     if not (ans is None):
     	ans.show2()
	elapsed = (time.time() - start)
	print "Time = %s" % elapsed	
	return elapsed;
     else:
     	print "Timeout waiting for %s" % packet[IP].src
	return -1 # si fallo mando -1 para saber que es un tiempo invalido


ping (sys.argv[1],1)

