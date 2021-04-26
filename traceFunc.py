#Jack Watson
#Used to import scapy's goods
from scapy.all import *
import sys


site = str(sys.argv[1])
ttl = int(sys.argv[2])


#print(sys.argv[1])

a,u = traceroute("google.com", maxttl=ttl)
print("Done")
#input('\nClick the "X" to Continue')



