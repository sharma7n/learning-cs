# Observer Interface

import lang
import abc

class Observer( object, metaclass = abc.ABCMeta ):
	
	@abc.abstractmethod
	def Update(data):
		raise NotImplementedError(lang.RequireImplementation("Update(data)"))