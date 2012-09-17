#!/usr/bin/python

from scapy.all import *


pkt = ARP(pdst=sys.argv[1], op="who-has");
response = sr1(pkt)
response.show()

