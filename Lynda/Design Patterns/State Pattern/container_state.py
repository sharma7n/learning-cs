# ContainerState interface

import abc

class ContainerState( object, metaclass = abc.ABCMeta ):
	
	@abc.abstractmethod
	def fill(content): raise NotImplementedError("Please implement the fill method to use this interface.")

	@abc.abstractmethod
	def empty(): raise NotImplementedError("Please implement the empty method to use this interface.")