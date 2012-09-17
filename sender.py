#!/usr/bin/python

import sys
from scapy.all import *

pkt = Ether() / ARP(pdst=sys.argv[1], op="who-has");
sendp(pkt)
