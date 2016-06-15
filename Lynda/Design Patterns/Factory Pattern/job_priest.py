# Priest class

from job import Job

class Priest( Job ):

	def __init__(self):
		self.name = "Priest"
		self.hp = 8
		self.strength = 1
		self.magic = 2
		self.speed = 0