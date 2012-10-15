#!/usr/bin/python

#Le paso como argumento la direccion ip y la cantidad. 

from scapy.all import *
from Ping import ping


for x in range(int(sys.argv[2])):
	time = ping(sys.argv[1]);
	if time != -1:
		print "Time = %s" % time	



