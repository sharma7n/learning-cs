# DarkFaerie decorator class

from neopet import Neopet
from neopet_decorator import NeopetDecorator

class DarkFaerie( NeopetDecorator ):

	def __init__(self, neopet):
		self.neopet = neopet
		self.SetAttributes()
		
	def SetAttributes(self):
		n = self.neopet
		print(n.GetName() + " was blessed by a Dark Faerie!")
		n.AddToScores(0, 0, 2, 0)