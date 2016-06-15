# ItemBag class

from item_set import ItemSet
from item_bag_iterator import ItemBagIterator

class ItemBag( ItemSet ):

	def __init__(self):
		self.items = set([])
		
	def add_item(self, item):
		self.items.add(item)
		
	def iterator(self):
		return ItemBagIterator(self)