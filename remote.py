# Save as server.py 
# Message Receiver
import os
from socket import *

# wysylanie komendy
host = "192.168.0.2"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
data = raw_input("podaj dane do wyslania:")
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

print data
UDPSock.close()
os._exit(0)