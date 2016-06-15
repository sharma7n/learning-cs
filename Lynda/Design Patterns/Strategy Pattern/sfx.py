# SFX interface

import abc

class SFX( object, metaclass = abc.ABCMeta ):

	@abc.abstractmethod
	def sound(self):
		raise NotImplementedError("Please implement the sound() method to use this interface.")