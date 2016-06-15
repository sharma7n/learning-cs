# AccessLocked Access class

from access_state import AccessState

class AccessLocked( AccessState ):

	def __init__(self, access):
		self.access = access

	def unlock(self):
		a = self.access
		a.access_state = a.access_closed
		print("Unlock successful! Unlocked.")
		return True
		
	def lock(self):
		print("Lock unsuccessful! Already locked.")
		return False
		
	def open(self):
		print("Open unsuccessful! Locked.")
		return False
		
	def close(self):
		print("Close unsuccessful! Already closed.")
		return False