# AccessClosed Access class

from access_state import AccessState

class AccessClosed( AccessState ):

	def __init__(self, access):
		self.access = access

	def unlock(self):
		print("Unlock unsuccessful! Already unlocked.")
		return False
		
	def lock(self):
		a = self.access
		a.access_state = a.access_locked
		print("Lock successful! Locked.")
		return True
		
	def open(self):
		a = self.access
		a.access_state = a.access_open
		print("Open successful! Opened.")
		return True
		
	def close(self):
		print("Close unsuccessful! Already closed.")
		return False