from linkedlist import LinkedList
from testcase import testcase, decoratecls, run_tests
# import unittest

@decoratecls(testcase)
class LinkedListTest():

	def test_create(self):
		"""Create empty list, single-item list, and multi-item list."""
		list1 = LinkedList()
		list2 = LinkedList(2)
		list3 = LinkedList(1, 2, "buckle my shoe")
		assert list1.size() == 0
		assert list2.size() == 1
		assert list3.size() == 3
		
	def test_append(self):
		"""Append to list at the top, append in the middle, and append bad items."""
		list1 = LinkedList()
		list2 = LinkedList(1, 2, 3)
		
		# Append to empty list at head position continuously.
		list1.append(0)
		list1.append(0, 0)
		list1.append(0, 1)
		assert list1 == LinkedList(0, 0, 0)
		
		list2.append(4, 1)
		assert list2 == LinkedList(1, 2, 4, 3)
		
		for bad_index in [-1, 0.2, 5, "foo"]:
			try:
				list2.append(5, bad_index)
				assert False
			except (IndexError, ValueError):
				assert True

	def test_remove(self):
		"""Remove from a multi-item list, remove from a single-item list, and remove from an empty list. 
		Append and remove. 
		Remove from the wrong index."""
		
		list1 = LinkedList()
		list2 = LinkedList(2)
		list3 = LinkedList(1, 2, "buckle my shoe")
		
		list3.remove(2)
		list3.remove(0)
		assert list3 == list2
	
	def test_get(self):
		pass
	
	def test_find(self):
		pass
		
	def test_size(self):
		pass

run_tests(LinkedListTest())