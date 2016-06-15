# ItemShopIterator class

from iterator import Iterator

class ItemShopIterator( Iterator ):

	def __init__(self, item_shop):
		self.stock = item_shop.stock
		self.keys_traversed = []
		
	def has_next(self): return len(self.keys_traversed) < len(self.stock)
	
	def next(self):
		new_stock = { i : self.stock[i] for i in self.stock.keys() }
		for k in self.keys_traversed: del new_stock[k]
		key, value = new_stock.popitem()
		self.stock[key] = value
		self.keys_traversed.append(key)
		return key, value