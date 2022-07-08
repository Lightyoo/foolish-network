from scapy.all import *

filter_info = str(input("# filter:"))
count = int(input("# count:"))

def packet_callback(pkt):
	print(pkt.show())	
	print(pkt.summary())
if count != 0:
	sniff(filter=filter_info,count=count,prn=packet_callback)
else:
	sniff(filter=filter_info,prn=packet_callback)