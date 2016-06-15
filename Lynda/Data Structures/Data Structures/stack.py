class Stack:

    def __init__(self):
        self._stack = []
		
    def push(self, value):
        self._stack.append(value)
		
    def peek(self):
        self._stack[-1]

    def pop(self):
	    self._stack.pop()
		
class PriorityQueue:

    def __init__(self)
		self._queue = {}
		self._occurrences = {}
		
    def push(self, value):
	    if self._occurrences[value] is None:
			self._occurrences[value] = 0
	    self._queue[value.order(), self._occurrences[value]] = value
		self._occurrences[value] += 1
		
	def pop(self):
        pop(self._queue[max(self._queue.keys())])