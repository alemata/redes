#!/usr/bin/python

from scapy.all import *

def tracerouteICMP(host):
  ipPkg = IP(dst=host,ttl=1) / ICMP() / 'test del tp'
  noTimeOut = True
  noRoute = True
  attempts = 3
  while noRoute:
    print "ttl = %d" %ipPkg.ttl

    response = sr1(ipPkg, timeout=2, verbose=0)

    if (response is None):
      attempts -= 1
      if (attempts == 0):
        attempts = 3
        ipPkg.ttl += 1
        print " * "

    else:
      # miro la direccion origen de la respuesta
      respSrc = response.src
      if (respSrc == host): #HABRIA QUE MIRAR EL TIPO?? SI ES ECHO-REPLY??
        noRoute = False
        print "Destino: " + respSrc
      # miro el tipo de respuestas ICMP
      # echo replay, por ahora encontre la ruta
      respType = response.payload.type
      if respType==1 :
        noRoute = False
      # por ahora los otros tpos de replay los tomamos similar al time exceeded
      if noRoute :
        print "Ruta: " + respSrc
        ipPkg.ttl += 1

tracerouteICMP(sys.argv[1])
