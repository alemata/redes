#!/usr/bin/python

#Le paso como argumento la direccion ip y la cantidad. 

from scapy.all import *
from Ping import ping

total = 0;
for x in range(int(sys.argv[2])):
	time = ping(sys.argv[1]);
	if time != -1:
		total = total + time;
		print "Time = %s" % time	
print "Promedio = %f" % (total / int(sys.argv[2]))



