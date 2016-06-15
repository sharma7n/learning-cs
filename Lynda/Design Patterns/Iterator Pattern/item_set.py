# ItemSet interface

import abc

class ItemSet( object, metaclass = abc.ABCMeta ):

	@abc.abstractmethod
	def iterator(): raise NotImplementedError("Please implement the iterator() method to use this interface.")