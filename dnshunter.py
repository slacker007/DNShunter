#! /usr/bin/env python
# created by slacker007
# @real_slacker007
# hunttools.org
# cybersyndicates.com
import pprint
import subprocess as sp
import socket
from struct import *
import datetime
import sys
import copy
import GeoIP
import socket
from re import search as reg_search
import hashlib
import argparse
from scapy.all import *
from scapy.layers.dns import DNSQR, DNSRR, DNS
'''
    Validate Dependencies & Install missing
'''
try:
        import impacket
        import dnslib
        from impacket import ImpactDecoder
except: 
        print "\nimpacket module is not installed on your system"
        print "Installing Impacket"
        p2 = sp.Popen('sudo -H pip install impacket dnslib', shell=True)
        p2.wait()
        import impacket
        from impacket import ImpactDecoder
        import dnslib

def main(args):
    '''
    DNSPARSER.. Extracts information from pcaps to aid in network attack analysis
    '''  
    gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

    if args.filename:
	cap = args.filename # passes value from argument into local variable
	try: # attempt to read pcap with scapy
	    pkts = rdpcap(cap)
	except Scapy_Exception: # if any error reading do the following
	    print "Unable to read [ {0} ]".format(cap) # print this
	    return 0 # exit program.. 
    elif args.interface:
        # Feature not complete
	return 0
      
    for p in pkts:
        if p.haslayer(DNS):
            if p.qdcount > 0 and isinstance(p.qd, DNSQR):
                query = p.qd.qname
                qtype = p.qd.qtype
                cntry = gi.country_name_by_name(query)
                result = "DNS [Q]: [S]:{:<15}\t[D]:{:<15}\t{:<}\t{:<}\t{:<}".format(p[IP].src, p[IP].dst, qtype, query, cntry)
            if p.ancount > 0 and isinstance(p.an, DNSRR):
                qresp = p.an.rrname
                rtype = p.an.type
                respdata = p.an.rdata
                alphabet = reg_search('[a-zA-Z]', respdata) # Search variable 'respdata' for any alpha chars
                if alphabet == None:
                    cntry = gi.country_name_by_addr(respdata) # Determine the country for the IP
                    result = "DNS [R]: [S]:{:<15}\t[D]:{:<15}\t{:<3}\t{:<}\t{:<}\t{:<}".format(p[IP].src, p[IP].dst, rtype, qresp, respdata, cntry)
                else:
                    result = "DNS [R]: [S]:{:<15}\t[D]:{:<15}\t{:<3}\t{:<}\t{:<}".format(p[IP].src, p[IP].dst, rtype, qresp, respdata)
            print result
        else:
            continue

if __name__ == "__main__":
    #parse arguments from cli
    if len(sys.argv) < 2:
        print "Error: Too Few Arguments"
        print "<command> --help"
        sys.exit()
    else:
        parser = argparse.ArgumentParser()
        #parser.add_argument('-l', '--listall', help='\tlist all available interfaces', action='store_true')
        parser.add_argument('-f', '--filename', type=str)
        #parser.add_argument('-i', '--interface', help='\tthe interface to listen on', type=str)
        args = parser.parse_args()
        main(args)
