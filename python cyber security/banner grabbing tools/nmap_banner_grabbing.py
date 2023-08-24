import nmap

ip_addr = "192.168.1.1"

def get_open_ports(ip_addr, ports_to_scan):
    nm = nmap.PortScanner()
    open_ports = []

    for port in ports_to_scan:
        result = nm.scan(ip_addr, str(port))
        if result['scan'][ip_addr]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    
    return open_ports

def get_service_info(ip_addr, port):
    nm = nmap.PortScanner()
    result = nm.scan(ip_addr, str(port))
    
    if result['scan'][ip_addr]['tcp'][port]['state'] == 'open':
        service_name = result['scan'][ip_addr]['tcp'][port]['name']
        service_version = result['scan'][ip_addr]['tcp'][port]['version']
        return f"Port {port}: Service: {service_name}, Version: {service_version}"
    else:
        return f"Port {port}: Port closed"

def main():
    ports_to_scan = range(1, 1001)  # Ports start from 1
    open_ports = get_open_ports(ip_addr, ports_to_scan)
    
    print("Open ports:")
    for port in open_ports:
        service_info = get_service_info(ip_addr, port)
        print(service_info)

if __name__ == "__main__":
    main()
