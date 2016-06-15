# Observable Twitter class

from subject import Subject

class Twitter( Subject ):

	def __init__(self, message):
		self.message = message
		self.observers = []
	
	def __str__(self):
		return self.message
		
	# Subject interface methods.
	
	def RegisterObserver(self, observer):
		self.observers.append(observer)
	
	def RemoveObserver(self, observer):
		i = self.observers.remove(observer)
		
	def NotifyObservers(self):
		for observer in self.observers:
			observer.Update(self.message)

	# End of Subject interface methods.
	
	def GetMessage(self):
		return self.message
		
	def SetMessage(self, message):
		self.message = message
		self.NotifyObservers()