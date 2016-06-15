# AccessOpen Access class

from access_state import AccessState

class AccessOpen( AccessState ):

	def __init__(self, access):
		self.access = access

	def unlock(self):
		print("Unlock unsuccessful! Already unlocked.")
		return False
		
	def lock(self):
		print("Lock unsuccessful! Already opened.")
		return False
		
	def open(self):
		print("Open unsuccessful! Already opened.")
		return False
		
	def close(self):
		a = self.access
		a.access_state = a.access_closed
		print("Close successful! Closed.")
		return True