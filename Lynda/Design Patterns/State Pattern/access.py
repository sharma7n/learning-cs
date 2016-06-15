# Access base class

from access_locked import AccessLocked
from access_closed import AccessClosed
from access_open import AccessOpen

class Access():

	def __init__(self):
		self.access_locked = AccessLocked(self)
		self.access_closed = AccessClosed(self)
		self.access_open = AccessOpen(self)
		self.access_state = self.access_locked
		
	def unlock(self): raise NotImplementedError("Please implement the unlock method to use this base class.")
		
	def lock(self): raise NotImplementedError("Please implement the lock method to use this base class.")
		
	def open(self): raise NotImplementedError("Please implement the open method to use this base class.")
		
	def close(self): raise NotImplementedError("Please implement the close method to use this base class.")