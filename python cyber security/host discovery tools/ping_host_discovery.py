from scapy.all import *
from multiprocessing import Pool

def ping_target(ip_address):
    ip = IP(dst=ip_address)
    icmp = ICMP()
    ping_packet = ip / icmp
    response = sr1(ping_packet, timeout=0.5, verbose=False)
    if response:
        return ip_address
    return None

def main():
    address_base = "10.0.2."
    target_addresses = [address_base + str(i) for i in range(256)]

    pool = Pool(processes=8)  # Adjust the number of processes as needed
    results = pool.map(ping_target, target_addresses)
    pool.close()
    pool.join()

    host_list = [ip for ip in results if ip is not None]
    print(host_list)

if __name__ == "__main__":
    main()
