# DNShunter
DNShunter is a python based module that is written for MercenaryHuntFramework &amp; Mercenary-Linux.  Currently it reads in .pcap files and extracts the DNS Queries and Answers.  In addition to extracting the queries &amp; answers, it also performs a geo-lookup of the domains &amp; the associated IP's.  This makes it easy to catch attacks such as DNS Cache Poisoning and DNSBeacons.  

***EXAMPLE:***
```
mercenary@ubuntu:~/Demo$ python dnshunter.py --help
WARNING: No route found for IPv6 destination :: (no default route?)
usage: dnshunter.py [-h] [-f FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
  
mercenary@ubuntu:~/Demo$ python dnshunter.py -f legitDNS.pcap
WARNING: No route found for IPv6 destination :: (no default route?)
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	tiles.services.mozilla.com.	United States
DNS [R]: [S]:192.168.6.2    	[D]:192.168.6.160  	5  	tiles.services.mozilla.com.	tiles.r53-2.services.mozilla.com.
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	tiles.services.mozilla.com.	United States
DNS [R]: [S]:192.168.6.2    	[D]:192.168.6.160  	5  	tiles.services.mozilla.com.	tiles.r53-2.services.mozilla.com.
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	ocsp.digicert.com.	United States
DNS [R]: [S]:192.168.6.2    	[D]:192.168.6.160  	5  	ocsp.digicert.com.	cs9.wac.phicdn.net.
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	start.ubuntu.com.	United Kingdom
DNS [R]: [S]:192.168.6.2    	[D]:192.168.6.160  	1  	start.ubuntu.com.	91.189.89.88	United Kingdom
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	start.ubuntu.com.	United Kingdom
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	soft-start.loop.services.mozilla.com.	None
DNS [R]: [S]:192.168.6.2    	[D]:192.168.6.160  	1  	start.ubuntu.com.	91.189.90.40	United Kingdom
DNS [Q]: [S]:192.168.6.160  	[D]:192.168.6.2    	1	tiles.cdn.mozilla.net.	United States

```
