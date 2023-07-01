import socket
    
def portscan(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host,port))
    if result == 0:
        print(f" this port {port} and IP {host} was successful")
    sock.close()
    
for ports in range(20,1000):
    host = "127.0.0.1"
    port = ports
    portscan(host, port)        