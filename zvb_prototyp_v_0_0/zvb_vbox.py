from vboxapi import VirtualBoxManager

def find_vms():
	vms = []	
	vbox = mgr.vbox
	for m in mgr.getArray(vbox, 'machines'):
		vms.append(m.name)
	print vms 
	return vms 

def start_vm(vmname):
	vbox = mgr.vbox
	mach = vbox.findMachine(vmname)
	session = mgr.getSessionObject(vbox)
	progress = mach.launchVMProcess(session, "gui", "")
	progress.waitForCompletion(-1)
	mgr.closeMachineSession(session)

def delete_vm(vmname):
	vbox = mgr.vbox
	machine = vbox.findMachine(vmname)
	machine.unregister(4)
	machine.deleteConfig([])
	return True

def create_vm(vmname, vmtype):
	vbox = mgr.vbox
	machine = vbox.createMachine("", vmname, [], vmtype, [])
	machine.savesettings()
	vbox.registerMachine(machine)
	return True

def find_known_hosts():
	known_hosts = []
	return known_hosts
	
mgr = VirtualBoxManager(None, None)
