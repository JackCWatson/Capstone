# Jack Watson
#API Creds go to macvendors.co
import pprint
import requests
import sys

num = int(sys.argv[1])
macs = []
for x in range(2, num + 2):
    macs.append(sys.argv[x])

MAC_URL = 'http://macvendors.co/api/%s'
for addr in macs:
    r = requests.get(MAC_URL % addr)
    pp = pprint.PrettyPrinter(width=50, compact=True)
    pp.pprint(r.json())

print("Done")



