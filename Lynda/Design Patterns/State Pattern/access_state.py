# AccessState interface

import abc

class AccessState( object, metaclass = abc.ABCMeta ):

	@abc.abstractmethod
	def unlock(self): raise NotImplementedError("Please implement the unlock method to use this interface.")
		
	@abc.abstractmethod
	def lock(self): raise NotImplementedError("Please implement the lock method to use this interface.")
		
	@abc.abstractmethod
	def open(self): raise NotImplementedError("Please implement the open method to use this interface.")
		
	@abc.abstractmethod
	def close(self): raise NotImplementedError("Please implement the close method to use this interface.")