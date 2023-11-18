import socket
from time import sleep
from sys import argv
from datetime import datetime

interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)

allips = [ip[-1][0] for ip in interfaces if ip[-1][0] != '127.0.0.1']
msg = b'TEST'

if len(argv)> 1:
    allips += argv[1:]

counter = 0

while True:
    for ip in allips:
        cur_time = datetime.now().time()
        counter+=1
        print(f'[{cur_time}] Sending from {ip} | #{counter}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip,0))
        sock.sendto(msg, ("255.255.255.255", 7720))
        sock.close()
    sleep(2)