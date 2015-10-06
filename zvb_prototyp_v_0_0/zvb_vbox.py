from vboxapi import VirtualBoxManager
import subprocess
import config

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

def start_vm(vmname):
	subprocess.Popen([config.vboxmanage_path, "startvm", vmname], stdout=subprocess.PIPE, shell=True)
	return True

def delete_vm(vmname):
	subprocess.Popen([config.vboxmanage_path, "unregistervm", vmname, "-delete"], stdout=subprocess.PIPE, shell=True)
	return True

def create_vm(vmname, vmtype):
	out2 = []
	proc = subprocess.Popen([config.vboxmanage_path, "createvm", "--name", vmname, "--ostype", vmtype], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	out2 = out.split('\n')[-2]
	subprocess.Popen([config.vboxmanage_path, "registervm", out2.split("'")[1]], stdout=subprocess.PIPE, shell=True)
	return True
def find_known_hosts():
	known_hosts =[]
	tab=[]
	temp = []
	proc = subprocess.Popen(["nmap", "--open", "-sn", config.ip], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	tab = out.split('\n')
	search_string = "Nmap scan report for"
	for i in tab:
		if search_string in i:
			temp = i.split(" ")
			known_hosts.append(temp[-1])
	return known_hosts
	
mgr = VirtualBoxManager(None, None)
