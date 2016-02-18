import os
from socket import *
import sys

host = sys.argv[1]
data = sys.argv[2]

# wysylanie komendy
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.sendto(data, addr)
if data == "exit":
	UDPSock.close()
	os._exit(0)
UDPSock.close()

#odbieranie odpowiedzi
host = "192.168.0.3"
port = 13000
addr = (host, port)
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
(data, addr) = UDPSock.recvfrom(buf)

UDPSock.close()