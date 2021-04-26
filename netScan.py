# Jack Watson
# This is a network scanning script made in scapy.
# Help from a few tutorials for various parts: thepythoncode.com, geeksforgeeks, scapy documentation
from scapy.all import *
import sys

#Add in macvendors api? ///////---------------------> Check this
#Vendors are added in seperate api


# This is the IP range that you will scan to see connected users
# /24 Indicates the range, common in subnetting
targetIpRange = str(sys.argv[1])

#"192.168.1.1/24" My range 
#"192.168.0.1/24" Wifi Range
#192.168.0.0/16 entire 1918 subnet range


# Next we have the creation of the packet that uses ARP protocol
# This is a communication protocol used for discovering addresses (Mac addresses and ips 
# Ethernet broadcast packet
arpPacket = ARP(pdst=targetIpRange)
etherPacket = Ether(dst="ff:ff:ff:ff:ff:ff")
totalPacket = etherPacket/arpPacket

#Send packets
result = srp(totalPacket, timeout=3, verbose=0)[0]

# List of whose on your network! Adds mac address and Ip
userList = []
for sent, received in result:
    # IP and Mac address added to each user
    userList.append({'ip': received.psrc, 'mac': received.hwsrc})


# print userList
print("Available devices in the network:")
print("IP" + " "*27+"MAC")
for client in userList:
    print("{:16}    {}".format(client['ip'], client['mac']))


#Input catch and Close provention
print("Done")
#input('\nClick the "X" to Continue')