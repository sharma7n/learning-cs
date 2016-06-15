# TreasureChest class

from access import Access
from access_locked import AccessLocked
from access_closed import AccessClosed
from access_open import AccessOpen

from container import Container
from container_empty import ContainerEmpty
from container_full import ContainerFull

class TreasureChest( Access, Container ):
		
	def __init__(self):
		self.access_locked = AccessLocked(self)
		self.access_closed = AccessClosed(self)
		self.access_open = AccessOpen(self)
		self.access_state = self.access_closed
		
		self.content = None
		self.content_empty = ContainerEmpty(self)
		self.content_full = ContainerFull(self)
		self.content_state = self.content_empty

	# Access methods
	
	def unlock(self): self.access_state.unlock()
	def lock(self): self.access_state.lock()
	def open(self): self.access_state.open()
	def close(self): self.access_state.close()

	# Container methods
	
	def empty(self):
		if self.access_state == self.access_closed:
			self.access_state.open()
			return self.content_state.empty()
		elif self.access_state == self.access_open:
			return self.content_state.empty()
		else:
			print("Empty unsuccessful! Locked.")
			return False

	def fill(self, content):
		if self.access_state == self.access_closed:
			self.access_state.open()
			self.content_state.fill(content)
		elif self.access_state == self.access_open:
			self.content_state.fill(content)
		else:
			print("Fill unsuccessful! Locked.")
			return False