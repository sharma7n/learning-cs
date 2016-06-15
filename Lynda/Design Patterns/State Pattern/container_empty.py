# ContainerEmpty ContainerState class

from container_state import ContainerState

class ContainerEmpty( ContainerState ):

	def __init__(self, container):
		self.container = container

	def empty(self):
		print("Empty unsuccessful! Already empty.")
		return False
		
	def fill(self, content):
		c = self.container
		c.content = content
		c.content_state = c.content_full
		print("Fill successful! Filled with " + str(content) + ".")
		return True