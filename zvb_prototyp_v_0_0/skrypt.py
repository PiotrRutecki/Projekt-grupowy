# Save as server.py 
# Message Receiver
import os
from socket import *
import subprocess

def receiver():
	host = "192.168.0.2"
	port = 13000
	buf = 1024
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
	print "Waiting to receive messages..."
	(data, addr) = UDPSock.recvfrom(buf)
	if data == "exit":
		global working
		working = False
	print "Received message: " + data
	komendy = []
	komendy = data.split(' ')
	print komendy
	proc = subprocess.Popen(komendy,stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print out
	global wynik
	wynik = out
	print wynik
	UDPSock.close()
	global flaga
	flaga = 1

# Save as client.py 
# Message Sender
def sender():
	host = "192.168.0.3" # set to IP address of target computer
	port = 13000
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	# data = raw_input("Enter message to send or type 'exit': ")
	# if data == "exit":
		# global working
		# working = False
	print "wysylam: " + wynik
	UDPSock.sendto(wynik, addr)
	UDPSock.close()
	global flaga
	flaga = 0

flaga = 0
working = True
wynik = ""

while working:
	cases = {0: receiver, 1: sender}
	cases[flaga]()
	