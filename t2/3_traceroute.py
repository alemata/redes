#!/usr/bin/python

from scapy.all import *


def tracerouteICMP(host):
	ipPkg = IP(dst=host,ttl=1) / ICMP() / 'test del tp'
	noTimeOut = True
	noRoute = True
	i =1
	attempts = 0
	while noRoute and noTimeOut :
		
		print "ttl = %d" %ipPkg.ttl
		response = sr1(ipPkg, timeout=20, verbose=0)
		if not (response is None):
			response.show()
			#miro la direccion origen de la respuesta
			respSrc = response.src
			if (respSrc == host): #HABRIA QUE MIRAR EL TIPO?? SI ES ECHO-REPLY??
				noRoute = False
				print "Destino: " + respSrc
			#miro el tipo de respuestas ICMP
			#echo replay, por ahora encontre la ruta
			respType = response.payload.type
			if respType==1 :
				noRoute = False
			#por ahora los otros tpos de replay los tomamos similar al time exceeded
			if noRoute :
				print "Ruta: " + respSrc
				i = i + 1
				ipPkg.ttl = i
		else:
			i = i + 1
			ipPkg.ttl = i
			print "Timeout waiting"
			#noTimeOut = False  
			
	if not (noTimeOut)	:
		print "Timeout waiting"
		
		
tracerouteICMP(sys.argv[1])
