 # Character class
 
class Character:
 
	def __init__(self, name, job):
		self.name = name
		self.job = None
		raise NotImplementedError("Please override the constructor to use this base class.")
		
	def create_job(self, job):
		raise NotImplementedError("Please override the create_job method to use this base class.")

	def status(self):
		print(self.name + " the " + self.job.name)
		print("HP: " + str(self.job.hp))
		print("Strength: " + str(self.job.strength))
		print("Magic: " + str(self.job.magic))
		print("Speed: " + str(self.job.speed))