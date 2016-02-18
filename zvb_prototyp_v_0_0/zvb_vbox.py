import subprocess
import config
import re

def find_vms():
	tab = []
	out_tab = []
	proc = subprocess.Popen([config.vboxmanage_path, "list", "vms"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	tab = out.split('\n')
	for i in tab:
		if i != "":
			out_tab.append(i.split('"')[1])
	return out_tab

def get_vbox_version():
	proc = subprocess.Popen([config.vboxmanage_path, "--version"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return out
	
def start_vm(vmname):
	try:
		subprocess.Popen([config.vboxmanage_path, "startvm", vmname], stdout=subprocess.PIPE, shell=True)
	except IOError, error:
		print error
		return False
	return True

def delete_vm(vmname):
	try:
		subprocess.Popen([config.vboxmanage_path, "unregistervm", vmname, "-delete"], stdout=subprocess.PIPE, shell=True)
	except IOError, error:
		print error
		return False
	return True

def create_vm(host, vmname, vmtype):
	try:
		out2 = []
		proc = subprocess.Popen([config.vboxmanage_path, "createvm", "--name", vmname, "--ostype", vmtype], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		out2 = out.split('\n')[-2]
		subprocess.Popen([config.vboxmanage_path, "registervm", out2.split("'")[1]], stdout=subprocess.PIPE, shell=True)
	except IOError, error:
		print error
		return False
	return True
def find_known_hosts():
	known_hosts =[]
	tab=[]
	temp = []
	proc = subprocess.Popen(["nmap", "--open", "-sn", config.ip], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	known_hosts = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', out)
	return known_hosts
	
def remote_command(host, command):
	#wysylanie polecenia
	host = host
	port = 8082
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.sendto(command, addr)
	UDPSock.close()

	#odbieranie odpowiedzi
	host = "localhost"
	port = 8082
	addr = (host, port)
	buf = 1024
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
	(data, addr) = UDPSock.recvfrom(buf)
	UDPSock.close()
	return data