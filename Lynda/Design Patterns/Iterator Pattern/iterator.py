# Iterator interface

import abc

class Iterator( object, metaclass = abc.ABCMeta ):

	@abc.abstractmethod
	def has_next(): raise NotImplementedError("Please implement the has_next() method to use this interface.")
	
	@abc.abstractmethod
	def next(): raise NotImplementedError("Please implement the next() method to use this interface.")