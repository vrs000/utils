import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.230.170", 7730)
# serverAddressPort   = ("localhost", 7730)



UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# UDPClientSocket.bind(('192.168.230.197', 11))

result = UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print(result)