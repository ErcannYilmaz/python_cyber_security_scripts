from scapy.all import *

host_list = []

def main():

	eth = Ether()
	arp = ARP()

	eth.dst = "ff:ff:ff:ff:ff:ff"
	arp.pdst = "10.0.2.0/24"

	bc_packet = eth/arp

	ans, unans = srp(bc_packet, timeout=0.5)

	for rcv, src in ans:
		host_list.append(f"{rcv.pdst} : {rcv.src}")

	print(host_list)

if __name__ == '__main__':
	main()
