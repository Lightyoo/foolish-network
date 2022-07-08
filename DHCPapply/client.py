from scapy.all import *

# Ether/IP/UDP/BOOTP/DHCP


# send DHCP Discover
mac_random = str(RandMAC())
Ether_Discover = Ether(src=mac_random,dst="ff:ff:ff:ff:ff:ff")

IP_Discover = IP(src="0.0.0.0",dst="255.255.255.255")

UDP_Discover = UDP(sport=68,dport=67)


# For DHCP Discover,chaddr->DHCP Client's Mac address
# xid Things Id

import binascii
import random

client_mac_id = binascii.unhexlify(mac_random.replace(":",""))
xid_random = random.randint(1,900000000)

BOOTP_Discover = BOOTP(chaddr=client_mac_id,xid=xid_random)

DHCP_Discover = DHCP(options=[("message-type","discover"),"end"])

Discover = Ether_Discover/IP_Discover/UDP_Discover/BOOTP_Discover/DHCP_Discover

sendp(Discover,iface="wlan0")


# def detect_dhcp(pkt):
# 	if DHCP in pkt:
# 		ls(pkt)

# sniff(filter="src port 67",iface=conf.iface,prn=detect_dhcp)

'''
Icant continue because
After I send DHCP Discover I cant receive DHCP Offer
and I cant know DHCP Server's address
'''