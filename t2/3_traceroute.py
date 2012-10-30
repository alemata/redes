#!/usr/bin/python

from scapy.all import *

def tracerouteICMP(host):
	ipPkg = IP(dst=host,ttl=1) / ICMP() / 'test del tp'
	noTimeOut = True
	noRoute = True
	while noRoute:
		if(ipPkg.ttl < 10):
			print " %d " %ipPkg.ttl,
		else:
			print "%d " %ipPkg.ttl,

		response = sr1(ipPkg, verbose=0, timeout=3, retry=3, inter=1)

		if (response is None):
			ipPkg.ttl += 1
			print "* * *"

		else:
			# miro la direccion origen de la respuesta
			respSrc = response.src

      # miro el tipo de respuestas ICMP y busco un echo replay 
			if response.payload.type == 0 :
				noRoute = False
				print response.src
				# por ahora los otros tpos de replay los tomamos similar al time exceeded

			if noRoute :
				print respSrc
				ipPkg.ttl += 1

tracerouteICMP(sys.argv[1])
