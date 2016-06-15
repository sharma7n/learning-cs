# Flaming decorator class

from neopet import Neopet
from neopet_decorator import NeopetDecorator

class Flaming( NeopetDecorator ):

	def __init__(self, neopet):
		self.neopet = neopet
		
	def GetSpecies(self):
		return "Flaming " + self.neopet.GetSpecies()