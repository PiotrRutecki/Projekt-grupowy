# Save as server.py 
# Message Receiver
import os
from socket import *
import sys
host = sys.argv[1]
data = sys.argv[2]
print data
# wysylanie komendy
#host = "192.168.0.2"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.sendto(data, addr)
if data == "exit":
	UDPSock.close()
	os._exit(0)
UDPSock.close()
