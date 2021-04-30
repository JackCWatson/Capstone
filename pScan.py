#Jack Watson
from scapy.all import *

userList = []
pTest = []

targetIpRange = str(sys.argv[1])
port_range = [21, 22, 23, 25, 53, 80, 135, 443, 1433, 3389]


arpPacket = ARP(pdst=targetIpRange)
etherPacket = Ether(dst="ff:ff:ff:ff:ff:ff")
totalPacket = etherPacket/arpPacket

result = srp(totalPacket, timeout=3, verbose=0)[0]


for sent, received in result:
    userList.append({'ip': received.psrc, 'mac': received.hwsrc})

# print userList
print("IP" + " "*16+"Port" + " "*7 + "Status")
for client in userList:
    host = client['ip']
    # Send Sync packet to every port in the range
    for dst_port in port_range:
        resp = sr1(
            IP(dst=host)/TCP(sport=8080,dport=dst_port),timeout=1,
            verbose=0,
        )

        if resp is None:
            pass

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12): #x12 -> port is open (Sync flag)
                # Close connection (Not neccessary but polite)
                send_rst = sr(
                    IP(dst=host)/TCP(sport=8080,dport=dst_port),
                    timeout=1,
                    verbose=0,
                )
                pTest.append({'host' : host, 'port' : dst_port, 'status' : "open"}) #Adds to new printing list
            elif (resp.getlayer(TCP).flags == 0x14): #x14 -> port closed (Reset flag)
                pass
     
 
    #Print the List
for chost in pTest:
    print('{:<14}    {:<5}      {:<4}'.format(chost['host'], chost['port'], chost['status']))


print('Done')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

