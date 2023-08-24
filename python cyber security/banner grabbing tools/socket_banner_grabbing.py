import socket
from multiprocessing import Pool

ip_addr = "192.168.1.1"

def scan_port(port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sckt.settimeout(3.0)
        sckt.connect((ip_addr, port))
        response = sckt.recv(1024)
        print(f"Port: {str(port)}: open \nService:{response.decode()}")
    except socket.timeout as e:
        if port == 80:
            try:
                http_message = "GET / HTTP/1.0\r\n\r\n"
                sckt.send(http_message.encode())
                http_response = sckt.recv(4096)
                print(f"Port: {str(port)}\nService:{http_response.decode()}")
            except Exception as e:
                print(f"Port: {str(port)}\nService: Can't detected!")
        else:
            print(f"Port: {str(port)}\nService: Can't detected!")
    except Exception as e:
        return None
    finally:
        sckt.close()

def main():
    pool = Pool(processes=8)  
    ports_to_scan = range(1000)
    open_ports = pool.map(scan_port, ports_to_scan)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
