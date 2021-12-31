#!/usr/bin/env python3

from scapy.all import ARP, Ether, srp
#from socket import *

range=input("Please Enter Your Target IP Range: ")
print("\n!!!Please Wait While We Scan The Network!!!")
arp=ARP(pdst=range)
bdcast=Ether(dst="ff:ff:ff:ff:ff:ff")
packet= bdcast/arp
targets=[]
tgtip=srp(packet, timeout=3, verbose=0)[0]
print("\nAVAILABLE DEVICES IN THE NETWORK:\n")
print(" "*5 + "IP" + " "*30 + "MAC")

for sent, received in tgtip:
    targets.append({'ip':received.psrc, 'mac':received.hwsrc})

for ip in targets:
    print(ip['ip'] + " "*18 + ip['mac'])
