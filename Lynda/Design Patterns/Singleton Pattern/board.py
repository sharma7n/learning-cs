# Board class (lazy, not thread-safe)
	
class Board:

	_internal = False # simulation of making a private constructor. It's still possible to change it... don't be a jerk.
	_instance = None # the unique instance.
	
	def __init__(self):
		if not Board._internal:
			raise Exception("This class cannot be instantiated. Please use the get_instance() method instead.")
		else:
			self.size = 19

	def get_instance():
		if Board._instance == None:
			Board._internal = True
			Board._instance = Board()
			Board._internal = False
		return Board._instance

	def set_size(self, new_size): self.size = new_size
	def get_size(self): return self.size