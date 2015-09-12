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
	pass

def create_vm(vmname, otherparams):
	pass

mgr = VirtualBoxManager(None, None)
	
