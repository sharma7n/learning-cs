# ItemBagIterator class

from iterator import Iterator

class ItemBagIterator( Iterator ):

	def __init__(self, item_bag):
		self.item_bag = item_bag.items
		self.taken = set([])
		
	def has_next(self): return len(self.item_bag - set(self.taken)) > 0
	
	def next(self):
		item = self.item_bag.pop()
		self.item_bag.add(item)
		self.taken.add(item)
		return item