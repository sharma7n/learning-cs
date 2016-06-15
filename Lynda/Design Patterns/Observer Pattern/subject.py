# Subject Interface

import lang
import abc

class Subject( object, metaclass = abc.ABCMeta ):
	
	@abc.abstractmethod
	def RegisterObserver(observer):
		raise NotImplementedError(lang.RequireImplementation("RegisterObserver(observer)"))
		
	@abc.abstractmethod
	def RemoveObserver(observer):
		raise NotImplementedError(lang.RequireImplementation("RemoveObserver(observer)"))
	
	@abc.abstractmethod
	def NotifyObservers():
		raise NotImplementedError(lang.RequireImplementation("NotifyObservers()"))