class LinkedList:
	def __init__(self, *args):
		self._value = None
		self._next = None
		self._size = 0
		for arg in args:
			self.append(arg)

	def _validate_index(self, index):
		"""Validates that the index given by the user is an integer between 0 and size - 1."""
		valid_index = index is int(index) and index >= 0 and index < self._size
		if not valid_index:
			raise IndexError()

	def _traverse(self, until = lambda i, list: True):
		"""Walks through the entire LinkedList and returns the last index and node.
		The 'until' lambda defines a continue condition for the traversal loop."""
		i = 0
		list = self
		while until(i, list) and list._next is not None:
			i += 1
			list = list._next
		return {"node_index" : i, "node" : list}

	def _to_pylist(self):
		"""Returns a standard python list where list[i] == MyLinkedList.get(i)."""
		pylist = []
		def record_values(i, list):
			pylist.append(list._value)
			return True
		self._traverse(record_values)
		return pylist

	def __str__(self):
		return str(self._to_pylist())
		
	def __eq__(self, other):
		"""Returns True if the two lists have the same sequences of values, i.e. if self.get(i) == other.get(i) for all i."""
		return self._to_pylist() == other._to_pylist()
		
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def _get_node(self, index):
		"""Returns the LinkedList node at the specified index."""
		self._validate_index(index)
		return self._traverse(lambda i, list: i < index)["node"]
		
	def append(self, value, index = None): # THIS SHOULD BE O(1)
		if index is not None:
			self._validate_index(index)
		if index == self._size - 1 or index is None:
			if self._size == 0:
				self._value = value
			else:
				new_node = LinkedList()
				new_node._value = value
				self._get_node(self._size - 1)._next = new_node
		else:
			node = self._get_node(index)
			new_node = LinkedList(value)
			new_node._next = node._next
			node._next = new_node
		self._size += 1
	
	def remove(self, index): # THIS SHOULD BE O(1)
		self._validate_index(index)
		if index > 0 and index < self._size - 1:
			node = self._get_node(index - 1)
			node._next = node._next._next
		elif index == 0:
			self = self._next
		else:
			node = self._get_node(index - 1)
			node._next = None
		self._size -= 1
			
	def get(self, index):
		self._validate_index(index)
		return self._get_node(index)._value
		
	def set(self, value, index):
		self._validate_index(index)
		node = self._get_node(index)
		node._value = value
		
	def find(self, value):
		index, node = self._traverse(lambda i, list: list._value != value)
		if index == self._size - 1 and node._value != value:
			return -1
		else:
			return index
		
	def size(self):
		return self._size