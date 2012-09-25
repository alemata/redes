#!/usr/bin/python

from scapy.all import *

import sys
sys.path.append('..')
sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/lib64/graphviz/python/')
import gv

# Import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.readwrite.dot import write

arps = rdpcap("mancuHome.pcap")


gr = digraph()


for x in arps:
	try:
		gr.add_nodes([x[ARP].psrc])
	except Exception, rr:
		pass
	

for x in arps:
	try:
		if x[ARP].op == 1:
			gr.add_edge((x[ARP].psrc, x[ARP].pdst))
	except Exception, rr:
		pass
	

# Draw as PNG
dot = write(gr)
gvv = gv.readstring(dot)
gv.layout(gvv,'dot')
gv.render(gvv,'png','arpGraph.png')



