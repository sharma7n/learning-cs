# ContainerFull ContainerState class

from container_state import ContainerState

class ContainerFull( ContainerState ):

	def __init__(self, container):
		self.container = container
		
	def empty(self):
		c = self.container
		content = c.content
		c.content_state = c.content_empty
		print("Empty successful! Emptied.")
		return content
	
	def fill(self, content):
		print("Fill unsuccessful! Already full.")
		return False
		
	