# Observer Web class

from observer import Observer
from display import Display

class Web( Observer, Display ):

	def __init__(self, feed):
		self.feed = feed
		self.message = feed.GetMessage()
		feed.RegisterObserver(self)
		
	# Observer interface method.
	def Update(self, new_message):
		self.message = new_message
		self.Display()
		
	# Display interface method.
	def Display(self):
		print("Twitter on the Web: " + self.message)
		
	def Tweet(self, tweet):
		self.feed.SetMessage(tweet)