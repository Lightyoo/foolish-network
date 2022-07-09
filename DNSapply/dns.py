# from scapy.all import *


# floor_ip = IP(dst="8.8.8.8") # src="124.223.190.218"

# floor_udp = UDP(dport=53)

# qd = DNSQR(qname="hp.com",qtype=1) #255 means ANY
# floor_dns = DNS(rd=1,qdcount=1,qd=qd)

# send(floor_ip/floor_udp/floor_dns)
# # print(dns_result.getlayer(DNS).fields["an"][1].fields['rdata'])

# import dns

# domain = 'www.qq.com'
# A = dns.resolver.query(domain,"A")

# sniff(filter="src port 53",prn=lambda x:x.command())