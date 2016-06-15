# ItemShop class

from item_set import ItemSet
from item_shop_iterator import ItemShopIterator

class ItemShop( ItemSet ):

	def __init__(self):
		self.stock = {}
		
	def add_item(self, item, cost):
		self.stock[item] = cost
	
	def iterator(self):
		return ItemShopIterator(self)