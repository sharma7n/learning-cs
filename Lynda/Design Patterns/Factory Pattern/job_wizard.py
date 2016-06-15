# Wizard class

from job import Job

class Wizard( Job ):

	def __init__(self):
		self.name = "Wizard"
		self.hp = 6
		self.strength = 0
		self.magic = 4
		self.speed = 1