#!/usr/bin/env python3

import pyfiglet
import ipaddress
import validators
from socket import *
out = pyfiglet.figlet_format("WELCOME TO MY PORT SCANNER")
print(out)

ipdom=input("Please Enter Your Target IP\Domain: ")

try:
    ip=ipaddress.ip_address(ipdom)
    print("\nPlease Wait While Ports Are Being Scanned\n")
    for port in range(1,65535):
        s=socket(AF_INET,SOCK_STREAM)
        conn=s.connect_ex((str(ip),port))
        if(conn==0):
            print('port %d: OPEN'%(port))
        s.close()
except ValueError:
    if(validators.domain(ipdom)==True):
        print("\nPlease Wait While Ports Are Being Scanned\n")
        ip=gethostbyname(ipdom)
        for port in range(1,65535):
            s=socket(AF_INET,SOCK_STREAM)
            conn=s.connect_ex((str(ip),port))
            if(conn==0):
                print('port %d: OPEN'%(port))
            s.close()
    else:
        print ("\nPlease Enter a Valid IP\Domain")
#except:
#    print("Please Enter a Valid IP\Domain")
#    exit()
