# Display Interface

import lang
import abc

class Display( object, metaclass = abc.ABCMeta ):
	
	@abc.abstractmethod
	def Display():
		raise NotImplementedError(lang.RequireImplementation("Display()"))