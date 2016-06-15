# Weapon class

class Weapon:

	def __init__(self, sfx, damage):
		self.sfx = sfx
		self.damage = damage
		
	def play_sfx(self):
		self.sfx.sound()
		
	def deal_damage(self):
		self.damage.deal()