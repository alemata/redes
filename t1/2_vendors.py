#!/usr/bin/python

from scapy.all import *

# Build the vendor dictionary
ins = open( "vendorsUtil.txt", "r" )
vendors_dict = {}
for line in ins:
    vendors_dict[line[0:8]] = line[9:-1] 
ins.close()

# Print pretty vendor
def arp_monitor_callback(pkt):
	vendor_prefix = pkt[ARP].hwsrc[0:8].upper()
	strr =  pkt[ARP].psrc + ": \t" + vendors_dict[vendor_prefix]
	print strr

if len(sys.argv) == 1:
	print "Listening for 5 seconds.."
	to = 5  # Default value
else:
	to = int(sys.argv[1]) 

sniff(prn=arp_monitor_callback, filter="arp", store=0, timeout=to)
