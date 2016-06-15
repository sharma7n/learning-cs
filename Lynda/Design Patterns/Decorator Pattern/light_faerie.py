# LightFaerie decorator class

from neopet import Neopet
from neopet_decorator import NeopetDecorator

class LightFaerie( NeopetDecorator ):

	def __init__(self, neopet):
		self.neopet = neopet
		self.SetAttributes()
		
	def SetAttributes(self):
		n = self.neopet
		print(n.GetName() + " was blessed by a Light Faerie!")
		n.AddToScores(1, 0, 0, 0)