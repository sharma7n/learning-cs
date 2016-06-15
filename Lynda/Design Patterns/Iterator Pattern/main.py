from item_shop import ItemShop
from item_bag import ItemBag

MyShop = ItemShop()
MyShop.add_item("Sword", 100)
MyShop.add_item("Spear", 150)
MyShop.add_item("Axe", 180)
MyShop.add_item("Excalibur", 200000)
MyShopIterator = MyShop.iterator()

MyBag = ItemBag()
MyBag.add_item("Potion")
MyBag.add_item("Magic Wand")
MyBag.add_item("Cool Shield")
MyBagIterator = MyBag.iterator()

ItemIterators = [MyShopIterator, MyBagIterator]
for iter in ItemIterators:
	while iter.has_next():
		item = iter.next()
		print(item)