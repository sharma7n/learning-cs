# Container base class

from container_empty import ContainerEmpty
from container_full import ContainerFull

class Container():

	def __init__(self):
		self.content = None
		self.content_empty = ContainerEmpty(self)
		self.content_full = ContainerFull(self)
		self.content_state = self.content_empty
	
	def empty(self): raise NotImplementedError("Please implement the empty method to use this interface.")
	
	def fill(self, content): raise NotImplementedError("Please implement the fill method to use this interface.")