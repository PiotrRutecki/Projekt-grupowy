import pymongo
import zvbDAO
import zvb_vbox
import bottle
import cgi
import os
from socket import *
import config


__author__='artur'

@bottle.route('/')
def zvb_index():
	global known_hosts
	local_vms = zvb.get_vms(config.ip_without_mask)
	local_vbox_version = zvb.get_vbox_version(config.ip_without_mask)
	remote_vms = {}
	for host in known_hosts:
		remote_vms[host] = zvb.get_vms(host)
	return bottle.template('zvb_template',dict(hostname=config.ip_without_mask,
												local_vms=local_vms, 
												local_vbox_version=local_vbox_version,
												known_hosts=known_hosts, 
												remote_vms=remote_vms))
	
@bottle.route('/starting_vm/<vmname>')
def start_vm(vmname):
	vmname = cgi.escape(vmname)
	zvb_vbox.start_vm(vmname)
	return bottle.template('starting_vm', dict(vmname=vmname))

@bottle.route('/delete_vm/<vmname>')
def delete_vm(vmname):
	hostname = "local"
	vmname = cgi.escape(vmname)
	zvb_vbox.delete_vm(vmname)
	zvb.remove_vm(hostname, vmname)
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
			remote_vms = zvb_vbox.remote_command(host, "vboxmanage list vms")
			remote_vbox_version = zvb_vbox.remote_command(host, "vboxmanage list vms")
			zvb.insert_vms(host, remote_vbox_version, remote_vms)
		except:
			print "nie udalo sie polaczyc"

bottle.debug(True)
bottle.run(host='localhost', port=8082)