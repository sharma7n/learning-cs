# Damage interface

import abc

class Damage( object, metaclass = abc.ABCMeta ):

	@abc.abstractmethod
	def deal(self):
		raise NotImplementedError("Please implement the deal() method to use this interface.")