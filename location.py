#Jack Watson
# Documentation https://ipwhois.io/documentation
from urllib.request import urlopen
import json
import sys

#ip = "68.20.12.40"

num = int(sys.argv[1])
ips = []
for x in range(2, num + 2):
    ips.append(sys.argv[x])

for ip in ips:
    # # Sending an API request
    response = urlopen("http://ipwhois.app/json/"+ip)
    ipgeolocation = json.load(response)
    
    # # Country code output, field "country_code"
    print(ipgeolocation["city"] + ", " + ipgeolocation["region"] + ": " + ipgeolocation["country_code"])
    
print("Done")
