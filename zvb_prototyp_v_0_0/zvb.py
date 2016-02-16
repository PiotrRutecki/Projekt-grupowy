import pymongo
import zvbDAO
import zvb_vbox
import bottle
import cgi
import os
from socket import *
import config
import subprocess
import re

__author__='artur'

@bottle.route('/')
def zvb_index():
	global known_hosts
	local_vms = zvb.get_vms(config.ip_without_mask)
	local_vbox_version = zvb.get_vbox_version(config.ip_without_mask)
	remote_vms = {}
	remote_vbox = {}
	for host in known_hosts:
		remote_vms[host] = zvb.get_vms(host)
		remote_vbox[host] = zvb.get_vbox_version(host)
	
	return bottle.template('zvb_template',dict(hostname=config.ip_without_mask,
												local_vms=local_vms, 
												local_vbox_version=local_vbox_version,
												known_hosts=known_hosts, 
												remote_vms=remote_vms,
												remote_vbox=remote_vbox))
	
@bottle.route('/starting_vm/<host>/<vmname>')
def start_vm(host, vmname):
	vmname = cgi.escape(vmname)
	host = cgi.escape(host)
	if host == config.ip_without_mask: zvb_vbox.start_vm(vmname)
	else:
		proc = subprocess.Popen(["C:\\Users\\admin\\Desktop\\projekt\\Projekt-grupowy\\remote_bez_odpowiedzi.py", host, "vboxmanage startvm " + vmname], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
	return bottle.template('starting_vm', dict(vmname=vmname))

@bottle.route('/delete_vm/<host>/<vmname>')
def delete_vm(host, vmname):
	#hostname = "local"
	vmname = cgi.escape(vmname)
	host = cgi.escape(host)
	zvb_vbox.delete_vm(vmname)
	if host == config.ip_without_mask: 
		zvb_vbox.delete_vm(vmname)
		zvb.remove_vm(host, vmname)
	else:
		proc = subprocess.Popen(["C:\\Users\\admin\\Desktop\\projekt\\Projekt-grupowy\\remote_bez_odpowiedzi.py", host, "vboxmanage unregistervm " + vmname + " -delete"], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		zvb.remove_vm(host, vmname)
	return bottle.template('delete_vm', dict(vmname=vmname))
	
@bottle.get('/create_vm/')
def create_vm():
	return bottle.template('create_vm', dict(vmname="", vmtype=""))
	
@bottle.post('/create_vm/')
def process_create_vm():
	hostname = "local"
	vmname = bottle.request.forms.get("vmname")
	vmtype = bottle.request.forms.get("vmtype")
	zvb_vbox.create_vm(vmname, vmtype)
	zvb.create_vm(hostname, vmname)
	bottle.redirect("/")
	
@bottle.post('/')
def refresh_known_hosts():
	global known_hosts
	known_hosts = zvb_vbox.find_known_hosts()
	bottle.redirect('/')
		

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.zvb

zvb = zvbDAO.ZvbDAO(database)
zvb.drop_database()

local_vms = zvb_vbox.find_vms()
local_vbox_version = zvb_vbox.get_vbox_version()
zvb.insert_vms(config.ip_without_mask, local_vbox_version, local_vms)

known_hosts = zvb_vbox.find_known_hosts()
print known_hosts
for host in known_hosts:
	if host != config.ip_without_mask:
		try:
			proc = subprocess.Popen(["C:\\Users\\admin\\Desktop\\projekt\\Projekt-grupowy\\remote.py", host, "vboxmanage list vms"], stdout=subprocess.PIPE, shell=True)
			(remote_vms_tmp, err) = proc.communicate()
			print remote_vms_tmp
			remote_vms_t = []
			#remote_vms = re.findall('\"([a-zA-Z0-9_])\"',remote_vms_tmp)
			remote_vms_t = remote_vms_tmp.split("\n")
			print remote_vms_t
			# print type(remote_vms)
			# print remote_vms
			# print remote_vms[0]
			remote_vms_t.pop(0)
			remote_vms_t.pop(-1)
			remote_vms_t.pop(-1)
			
			print remote_vms_t
			remote_vms = []
			for i in remote_vms_t:
				remote_vms.append(i.split('"')[1])
			print remote_vms
			proc = subprocess.Popen(["C:\\Users\\admin\\Desktop\\projekt\\Projekt-grupowy\\remote.py", host, "vboxmanage --version"], stdout=subprocess.PIPE, shell=True)
			(remote_vbox_version_tmp, err) = proc.communicate()
			remote_vbox_version = []
			remote_vbox_version = remote_vbox_version_tmp.split("\n")
			#remote_vbox_version_tmp.pop(0)
			#remote_vbox_version_tmp.pop(-1)
			#remote_vbox_version_tmp.pop(-1)
			zvb.insert_vms(host, remote_vbox_version[1], remote_vms)
		except IOError, error:
			print error 

bottle.debug(True)
bottle.run(host='localhost', port=8082)