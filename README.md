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
```
