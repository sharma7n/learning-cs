from character_fighter import Fighter
from character_mage import Mage

f1 = Fighter("Max", "dps")
f2 = Fighter("Ella", "tank")
m1 = Mage("Jasper", "dps")
m2 = Mage("Molly", "tank")

characters = [f1, f2, m1, m2]
for character in characters:
	character.status()