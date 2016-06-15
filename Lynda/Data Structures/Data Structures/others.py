class MyDict:

	def __init__(self):
		self._list = []

	def _my_hash(self, key):
		return hash(key)
	
	def set(self, key, value):
		self._list[self._my_hash(key)] = value
		
	def get(self, key):
		return self._list[self._my_hash(key)]
		
class MySet:

	def __init__(self):
		self._mydict = {}
		
	def add(self, value):
		self._mydict[value] = value
		
	def exists(self, value):
		return self._mydict[value] is not None
		
class BinarySearchTree:

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def add(self, value):
	    """Recursively add an element to the tree. Terminates in O(n) for unsorted, O(log n) for sorted."""
		
		# Base step.
	    if self = None:
		    self = BinarySearchTree(value)
		# Recursive step.
		else:
		    if value < self._value:
			    next = self._left
			else:
			    next = self._right
			if next is None:
			    next = BinarySearchTree(value)
			else:
			    next.add(value)
				
	def find(self, value):
		"""Recursively search tree for a value."""
		
		if value == self._value:
		    return True
		elif self is None:
			return True
		else:
		    if value < self._value:
			    self._left.find(value)
			else:
			    self._right.find(value)
	
	def list(self):
		"""Transform tree to ordered list."""
		
		my_list = []
		
		if self._left is not None:
			my_list.extend(self._left.list())
			
		my_list.extend(self._value)
		
		if self._right is not None:
		    my_list.extend(self._right.list())	
			
		return my_list
		
class MyMaxHeap:

	def __init__(self):
		self._list = []
		
	def _parent(self, index):
	    return 0
	
	def _swap(self, x, y):
		pass
		
	def add(self):
		heap = self._list
	    heap.append(value)
		last = len(self._list) - 1
		while heap[last] < heap[self._parent(last)]:
            self._swap(last, self._parent(last))
            last = self._parent(last)
		
class Graph:

    def __init__(self):
	    self._nodes = set([])
		self._edges = set([])
		
	def add_node(self, node):
	    self._nodes.add(node)
		
	def add_edge(self, node1, node2):
	    if node1 not in self._nodes:
		    raise ValueError("First node is not in the graph!")
		if node2 not in self._nodes:
		    raise ValueError("Second node is not in the graph!")
		self._edges.add((node1, node2))
		self._edges.add((node2, node1))
		
	def get_neighbors(self, node):
	    if node not in self._nodes:
		return set([edge[1] for edge in self._edges if edge[0] == node])
		    raise ValueError("Node is not in the graph!")