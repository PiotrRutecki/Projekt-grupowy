__author__ = 'artur'

#DATA ACCESS OBJECT

class ZvbDAO:
	def __init__(self, database):
		self.db = database
		self.zvb = database.zvb
	
	def drop_database(self):
		try:
			self.zvb.drop()
		except pymongo.errors.OperationFailure:
			print "oops, mongo error"
			return False
		return True
		
	def insert_vms(self, vms):
		insertion = { "host": "local", "vms_names": vms}
		try:
			self.zvb.insert(insertion)
		except pymongo.errors.OperationFailure:
			print "oops, mongo error"
			return False
		return True
		
	def get_vms(self, hostname):
		vms_on_host = []
		cursor = self.zvb.find({'host':hostname})
		for name in cursor:
			vms_on_host.append(name['vms_names'])
		
		return vms_on_host
		
	def create_vm(self, hostname, vmname):
		try:
			self.zvb.update({'host':hostname},{'$push':{'vms_names':vmname}})
		except pymongo.errors.OperationFailure:
			print "oops, mongo error"
			return False
		return True
		
	def remove_vm(self, hostname, vmname):
		try:
			self.zvb.update({'host':hostname},{'$pull':{'vms_names':vmname}})
		except pymongo.errors.OperationFailure:
			print "oops, mongo error"
			return False
		return True
		
	def get_remote_vms(known_hosts):
		#z bazy scczytujemy hosty i ich vmki
		pass