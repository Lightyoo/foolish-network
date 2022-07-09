from scapy.all import *


def icmp_find(target_ip,timeout=1):
	icmp_ip = IP(dst=target_ip)
	icmp = icmp_ip/ICMP()

	ans = sr1(icmp,timeout=timeout)

	if ans:
		print(icmp_ip.dst,"is alive")
		return True

def tcp_find(target_ip,timeout=1):
	tcp = IP(dst=target_ip)/TCP(dport=80,flags="S")

	ans = sr1(tcp,timeout=timeout)

	if ans:
		print(f"{tcp.dst} is alive")
		return True

