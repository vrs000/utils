from datetime import datetime
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 7720))
while True:    
    data, addr = sock.recvfrom(1024)
    cur_time = datetime.now().time()
    print(f"{cur_time}: received {len(data)} bytes from {addr[0]}:{addr[1]}")
    