# Archer class

from job import Job

class Archer( Job ):

	def __init__(self):
		self.name = "Archer"
		self.hp = 8
		self.strength = 3
		self.magic = 0
		self.speed = 2