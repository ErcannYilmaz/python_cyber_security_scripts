import socket
from multiprocessing import Pool

ip_addr = "192.168.1.1"

def scan_port(port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sckt.connect((ip_addr, port))
        print(f"Port: {str(port)}: open")
    except Exception as e:
        return None
    finally:
        sckt.close()

def main():
    pool = Pool(processes=8)  # İhtiyaca göre işlemci çekirdek sayısını ayarlayın
    ports_to_scan = range(1000)
    open_ports = pool.map(scan_port, ports_to_scan)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()


	